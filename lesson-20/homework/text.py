import pandas as pd
import sqlite3

conn = sqlite3.connect("chinook.db")

customers = pd.read_sql_query("""
    SELECT c.CustomerId, c.FirstName || ' ' || c.LastName AS CustomerName, 
           SUM(i.Total) AS TotalSpent
    FROM Customer c
    JOIN Invoice i ON c.CustomerId = i.CustomerId
    GROUP BY c.CustomerId
    ORDER BY TotalSpent DESC
""", conn)

top5_customers = customers.head(5)

invoice_items = pd.read_sql_query("""
    SELECT ii.InvoiceId, ii.TrackId, t.AlbumId, i.CustomerId
    FROM InvoiceLine ii
    JOIN Track t ON ii.TrackId = t.TrackId
    JOIN Invoice i ON ii.InvoiceId = i.InvoiceId
""", conn)

album_track_counts = pd.read_sql_query("""
    SELECT AlbumId, COUNT(TrackId) AS TotalTracks
    FROM Track
    GROUP BY AlbumId
""", conn)

merged = invoice_items.merge(album_track_counts, on='AlbumId', how='left')

customer_album = merged.groupby(['CustomerId', 'AlbumId']).agg(
    purchased_tracks=('TrackId', 'nunique'),
    total_tracks=('TotalTracks', 'max')
).reset_index()

customer_album['FullAlbum'] = customer_album['purchased_tracks'] == customer_album['total_tracks']

customer_pref = customer_album.groupby('CustomerId')['FullAlbum'].any().reset_index()
customer_pref['Preference'] = customer_pref['FullAlbum'].apply(lambda x: 'Full Album' if x else 'Individual Tracks')

pref_summary = customer_pref['Preference'].value_counts(normalize=True) * 100

conn.close()

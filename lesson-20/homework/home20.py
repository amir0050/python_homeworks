import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")

invoices = pd.read_sql("SELECT InvoiceId, CustomerId, Total FROM Invoice", conn)
customers = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM Customer", conn)
invoice_totals = invoices.groupby("CustomerId")["Total"].sum().reset_index()
invoice_totals = invoice_totals.merge(customers, on="CustomerId")
top5 = invoice_totals.sort_values("Total", ascending=False).head(5)[["CustomerId","FirstName","LastName","Total"]]
print(top5)

invoice_lines = pd.read_sql("SELECT InvoiceLineId, InvoiceId, TrackId FROM InvoiceLine", conn)
tracks = pd.read_sql("SELECT TrackId, AlbumId FROM Track", conn)

invoice_tracks = invoice_lines.merge(tracks, on="TrackId").merge(invoices[["InvoiceId","CustomerId"]], on="InvoiceId")

album_track_counts = tracks.groupby("AlbumId")["TrackId"].nunique().reset_index().rename(columns={"TrackId":"TotalTracks"})
customer_album_tracks = invoice_tracks.groupby(["CustomerId","AlbumId"])["TrackId"].nunique().reset_index().rename(columns={"TrackId":"PurchasedTracks"})
merged = customer_album_tracks.merge(album_track_counts, on="AlbumId")
merged["FullAlbum"] = merged["PurchasedTracks"] == merged["TotalTracks"]

customer_pref = merged.groupby("CustomerId")["FullAlbum"].any().reset_index()
customer_pref["Preference"] = customer_pref["FullAlbum"].apply(lambda x: "Full Album" if x else "Individual Tracks")

summary = customer_pref["Preference"].value_counts(normalize=True) * 100
print(summary)

conn.close()

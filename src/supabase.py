import os
import supabase

SUPABASE_URL = 'https://cmikchdpocvhalnttdxg.supabase.co'
SUPABASE_KEY = 'sb_publishable_q2PoEj1kOaxNu_CBMrIVUg_LkfTZ2Wt'

os.environ['SUPABASE_URL'] = SUPABASE_URL
os.environ['SUPABASE_KEY'] = SUPABASE_KEY

from supabase import create_client

client = supabase.create_client(SUPABASE_URL,SUPABASE_KEY)

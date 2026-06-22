import { createClient } from '@supabase/supabase-js';
const supabaseUrl = 'https://uyvcewrjsghtuwdnvbuh.supabase.co';
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV5dmNld3Jqc2dodHV3ZG52YnVoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE0OTUxMjQsImV4cCI6MjA5NzA3MTEyNH0.AAuHdeDg3sh00e9hJRtHr4oOeSuSXqOPbAz0nCDJ2A8';

export const supabase = createClient(supabaseUrl, supabaseKey);    

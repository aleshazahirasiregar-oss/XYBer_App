def check_update_policy(package_name):
    try:
        if not isinstance(package_name, str):
            raise ValueError("Input harus berupa nama paket (string)")
            
        google_apps = ["com.google.android.gms", "com.google.android.play.games", "com.google.android.apps.maps", "com.google.android.youtube"]
        
        if package_name in google_apps:
            return "REDIRECT_TO_PLAYSTORE"
        return "ALLOW_INTERNAL_UPDATE"
    except Exception as e:
        return f"ERROR: {str(e)}"

def check_beta_slots(current_users):
    try:
        MAX_BETA = 999
        if current_users > MAX_BETA:
            return "BETA_FULL"
        return "SHOW_JOIN_BUTTON"
    except TypeError:
        return "ERROR: Format jumlah user tidak valid"


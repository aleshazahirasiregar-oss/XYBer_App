def check_update_policy(package_name):
    google_apps = ["com.google.android.gms", "com.google.android.play.games", "com.google.android.apps.maps", "com.google.android.youtube"]
    
    if package_name in google_apps:
        return "REDIRECT_TO_PLAYSTORE"
    else:
        return "ALLOW_INTERNAL_UPDATE"

def check_beta_slots(current_users):
    MAX_BETA = 999
    if current_users < MAX_BETA:
        return "SHOW_JOIN_BUTTON"
    else:
        return "BETA_FULL"


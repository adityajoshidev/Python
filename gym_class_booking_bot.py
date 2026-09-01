import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

ACCOUNT_EMAIL = "hello@test.com"  # The email you registered with
ACCOUNT_PASSWORD = "hellohi"      # The password you used during registration
GYM_URL = "https://appbrewery.github.io/gym/"

edge_options=webdriver.EdgeOptions()
edge_options.add_experimental_option("detach",True)

user_data_dir=os.path.join(os.getcwd(),"edge_profile")
edge_options.add_argument(f"--user-data-dir={user_data_dir}")

driver=webdriver.Edge(edge_options)
driver.get(GYM_URL)
def retry(func):
        func()
WebDriverWait(driver,10).until(ec.presence_of_element_located((By.ID, "login-button"))).click()
WebDriverWait(driver,10).until(ec.presence_of_element_located((By.ID, "email-input"))).send_keys(ACCOUNT_EMAIL)
driver.find_element(By.ID,value="password-input").send_keys(ACCOUNT_PASSWORD)
def login():
    driver.find_element(By.ID,value="submit-button").click()
    try:
        WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH, '//*[@id="schedule-link"]')))
    except Exception:
        retry(login)
login()

all_days=driver.find_elements(By.CLASS_NAME,value="Schedule_dayGroup__y79__")
classes_booked=0
waitlists_joined=0
already_booked_or_waitlisted=0
tue_thu_6pm_classes_processed=0
detailed_class_list=[]




for day in all_days:
    day_id=day.get_attribute("id")
    if "tue" in day_id or "thu" in day_id:
        all_classes=WebDriverWait(driver,10).until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,f"[id='{day_id}'] div")))
        day_title_id=day_id.replace("group","title")
        day_title=driver.find_element(By.ID,day_title_id).text
        for classes in all_classes:
            class_id=classes.get_attribute("id")
            if "1800" in class_id:
                tue_thu_6pm_classes_processed+=1
                button=driver.find_element(By.CSS_SELECTOR,f"#{classes.get_attribute("id")} div div.ClassCard_cardActions__tVZBm button")
                button_class=button.get_attribute("class")
                class_name=driver.find_element(By.ID,class_id.replace("card","name")).text
                if "booked" in button_class:
                    print(f"✓ Already booked: {class_name} on {day_title}")
                    detailed_class_list.append(f"  • [Already Booked] {class_name} on {day_title}")
                    already_booked_or_waitlisted+=1
                elif "waitlisted" in button_class:
                    print(f"✓ Already on waitlist: {class_name} on {day_title}")
                    detailed_class_list.append(f"  • [Already Waitlisted] {class_name} on {day_title}")
                    already_booked_or_waitlisted+=1
                else:
                    def button_click():
                        WebDriverWait(driver,50).until(ec.element_to_be_clickable(button)).click()
                        time.sleep(2)
                        if "booked" in driver.find_element(By.CSS_SELECTOR,f"#{classes.get_attribute("id")} div div.ClassCard_cardActions__tVZBm button").get_attribute("class"):
                            if "waitlist" in button_class:
                                print(f"✓ Joined waitlist for: {class_name} on {day_title}")
                                detailed_class_list.append(f"  • [New Waitlist] {class_name} on {day_title}")
                                global waitlists_joined
                                waitlists_joined+=1
                            else:
                                print(f"✓ Successfully Booked: {class_name} on {day_title}")
                                detailed_class_list.append(f"  • [New Booking] {class_name} on {day_title}")
                                global classes_booked
                                classes_booked+=1
                        else:
                            retry(button_click)
                    button_click()
                break

# print(f'''--- BOOKING SUMMARY ---
# New bookings: {classes_booked}
# New waitlist entries: {waitlists_joined}
# Already booked/waitlisted: {already_booked_or_waitlisted}
# Total Tuesday & Thursday 6pm classes: {tue_6pm_classes_processed}
# --- DETAILED CLASS LIST ---''')
# for i in detailed_class_list:
#     print(i)

print(f'''--- Total Tuesday/Thursday 6pm classes: {tue_thu_6pm_classes_processed} ---
 
--- VERIFYING ON MY BOOKINGS PAGE ---''')
def get_my_bookings():
    try:
        driver.find_element(By.XPATH,'//*[@id="my-bookings-link"]').click()
        booking_data=driver.find_elements(By.TAG_NAME,"p")
        booking_data=booking_data[::3]
        booking_titles=driver.find_elements(By.TAG_NAME,"h3")
        booking_count=0
        for i in range(len(booking_data)):
            data=booking_data[i]
            booking_schedule=data.text
            if "Tue" in booking_schedule or "Thu" in booking_schedule:
                if "6:00 PM" in booking_schedule:
                    print(f'''  ✓ Verified: {booking_titles[i].text}''')
                    booking_count+=1
        print(f'''--- VERIFICATION RESULT ---
        Expected: {tue_thu_6pm_classes_processed} bookings
        Found: {booking_count} bookings''')
        if tue_thu_6pm_classes_processed==booking_count:
            print(f"✅ SUCCESS: All bookings verified!")
        else:
            print(f"❌ MISMATCH: Missing {tue_thu_6pm_classes_processed-booking_count} bookings")
    except Exception:
        retry(get_my_bookings)
get_my_bookings()
driver.quit()

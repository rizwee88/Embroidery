# import streamlit as st

# # Title of the app
# st.title("📏 Unit Converter App")
# st.subheader("Easily convert between different units!")

# # Sidebar menu
# conversion_type = st.sidebar.radio("Choose a conversion type:", ["Length", "Weight", "Temperature"])

# # ---------------- Length Converter ----------------
# def length_converter():
#     st.header("📏 Length Converter")
#     units = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Miles": 0.000621371, "Feet": 3.28084}
    
#     amount = st.number_input("Enter length:", min_value=0.0, value=1.0)
#     from_unit = st.selectbox("From:", list(units.keys()))
#     to_unit = st.selectbox("To:", list(units.keys()))

#     if st.button("Convert"):
#         result = amount * (units[to_unit] / units[from_unit])
#         st.success(f"{amount} {from_unit} = {result:.4f} {to_unit}")

# # ---------------- Weight Converter ----------------
# def weight_converter():
#     st.header("⚖️ Weight Converter")
#     units = {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274}
    
#     amount = st.number_input("Enter weight:", min_value=0.0, value=1.0)
#     from_unit = st.selectbox("From:", list(units.keys()))
#     to_unit = st.selectbox("To:", list(units.keys()))

#     if st.button("Convert"):
#         result = amount * (units[to_unit] / units[from_unit])
#         st.success(f"{amount} {from_unit} = {result:.4f} {to_unit}")

# # ---------------- Temperature Converter ----------------
# def temperature_converter():
#     st.header("🌡 Temperature Converter")
#     temp_units = ["Celsius", "Fahrenheit", "Kelvin"]

#     amount = st.number_input("Enter temperature:", value=0.0)
#     from_unit = st.selectbox("From:", temp_units)
#     to_unit = st.selectbox("To:", temp_units)

#     if st.button("Convert"):
#         result = None
#         if from_unit == to_unit:
#             result = amount
#         elif from_unit == "Celsius":
#             if to_unit == "Fahrenheit":
#                 result = (amount * 9/5) + 32
#             elif to_unit == "Kelvin":
#                 result = amount + 273.15
#         elif from_unit == "Fahrenheit":
#             if to_unit == "Celsius":
#                 result = (amount - 32) * 5/9
#             elif to_unit == "Kelvin":
#                 result = (amount - 32) * 5/9 + 273.15
#         elif from_unit == "Kelvin":
#             if to_unit == "Celsius":
#                 result = amount - 273.15
#             elif to_unit == "Fahrenheit":
#                 result = (amount - 273.15) * 9/5 + 32
        
#         st.success(f"{amount} {from_unit} = {result:.2f} {to_unit}")

# # Execute the selected conversion function
# if conversion_type == "Length":
#     length_converter()
# elif conversion_type == "Weight":
#     weight_converter()
# elif conversion_type == "Temperature":
#     temperature_converter()

# # Footer
# st.sidebar.write("Made with ❤️ using Streamlit")
# import streamlit as st
# import pandas as pd
# from datetime import datetime
# from reportlab.pdfgen import canvas

# # ---- CONFIGURATION ----
# st.set_page_config(page_title="Lasani Embroidery - Monthly Stitch Report", page_icon="🧵", layout="wide")

# # ---- COMPANY HEADER ----
# st.markdown("""
#     <style>
#         .header { font-size:32px; font-weight:bold; color:#4CAF50; text-align:center; }
#         .sub-header { font-size:20px; font-weight:bold; color:#FF9800; text-align:center; }
#         .info-box { background-color:#f4f4f4; padding:10px; border-radius:5px; text-align:center; }
#         .footer { text-align:center; font-size:14px; color:#888; margin-top:20px; }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown('<div class="header">🧵 Lasani Embroidery - Monthly Stitch Report & Bonus Calculator</div>', unsafe_allow_html=True)
# st.markdown('<div class="sub-header">📌 Track Daily Stitch Production, Earnings & Bonus</div>', unsafe_allow_html=True)

# st.divider()

# # ---- CONSTANTS ----
# COST_PER_100K_STITCHES = 250  # Rs. 250 per 100,000 stitches
# BONUS_THRESHOLD = 400000  # Bonus given after 400,000 stitches per day
# BONUS_AMOUNT = 100  # Rs. 100 bonus if stitches exceed 400,000 per day

# # ---- SESSION STATE FOR MONTHLY DATA ----
# if "monthly_data" not in st.session_state:
#     st.session_state.monthly_data = []

# # ---- USER INPUTS ----
# st.subheader("📋 Employee & Machine Details")

# employee_name = st.text_input("👤 Employee Name", placeholder="Enter worker's name")
# machine_number = st.text_input("⚙️ Machine Number", placeholder="Enter machine number")
# attendance = st.radio("📅 Attendance", ["Present", "Absent"], index=0, horizontal=True)
# shift_time = st.selectbox("⏰ Shift Duration", ["Day Shift (8 AM - 8 PM)", "Night Shift (8 PM - 8 AM)"])
# stitch_count = st.number_input("🧵 Enter total stitches for today:", min_value=0, value=100000, step=1000)

# # ---- CALCULATION LOGIC ----
# cost = (stitch_count / 100000) * COST_PER_100K_STITCHES
# bonus = BONUS_AMOUNT if stitch_count >= BONUS_THRESHOLD else 0
# total_earning = cost + bonus

# # ---- SAVE DAILY RECORD ----
# if st.button("💰 Save Today's Record"):
#     if employee_name.strip() == "" or machine_number.strip() == "":
#         st.warning("⚠️ Please enter both the employee's name and machine number.")
#     else:
#         today_date = datetime.now().strftime("%Y-%m-%d")
#         st.session_state.monthly_data.append({
#             "Date": today_date,
#             "Employee": employee_name,
#             "Machine": machine_number,
#             "Shift": shift_time,
#             "Attendance": attendance,
#             "Stitches": stitch_count,
#             "Base Cost": round(cost, 2),
#             "Bonus": round(bonus, 2),
#             "Total Earnings": round(total_earning, 2)
#         })
#         st.success(f"✅ Record saved for {today_date}")

# # ---- SHOW MONTHLY REPORT ----
# st.subheader("📊 Monthly Stitch Report")
# if len(st.session_state.monthly_data) > 0:
#     df = pd.DataFrame(st.session_state.monthly_data)
#     st.dataframe(df)

#     # Calculate Total Monthly Summary
#     total_stitches = df["Stitches"].sum()
#     total_base_cost = df["Base Cost"].sum()
#     total_bonus = df["Bonus"].sum()
#     total_earnings = df["Total Earnings"].sum()

#     st.markdown(f"""
#     ### 📅 Monthly Summary
#     - 🧵 **Total Stitches:** {total_stitches:,}
#     - 💵 **Total Base Cost:** Rs. {total_base_cost:,.2f}
#     - 🎁 **Total Bonus Earned:** Rs. {total_bonus:,.2f}
#     - 💰 **Total Earnings:** Rs. {total_earnings:,.2f}
#     """)

#     # ---- PRINT MONTHLY REPORT FUNCTION ----
#     def generate_monthly_pdf():
#         pdf_filename = f"Lasani_Embroidery_Report_{datetime.now().strftime('%Y-%m')}.pdf"
#         c = canvas.Canvas(pdf_filename)
        
#         c.setFont("Helvetica-Bold", 16)
#         c.drawString(150, 800, "Lasani Embroidery - Monthly Stitch Report")
        
#         c.setFont("Helvetica", 12)
#         c.drawString(50, 770, f"Report Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
#         c.drawString(50, 750, f"Employee: {employee_name}")
#         c.drawString(50, 730, f"Machine Number: {machine_number}")
        
#         c.drawString(50, 700, f"Total Stitches: {total_stitches:,}")
#         c.drawString(50, 680, f"Total Base Cost: Rs. {total_base_cost:,.2f}")
#         c.drawString(50, 660, f"Total Bonus: Rs. {total_bonus:,.2f}")
#         c.drawString(50, 640, f"Total Earnings: Rs. {total_earnings:,.2f}")

#         c.drawString(50, 610, "Daily Breakdown:")
#         y_pos = 590
#         for index, row in df.iterrows():
#             c.drawString(50, y_pos, f"{row['Date']} - {row['Stitches']} stitches - Rs. {row['Total Earnings']:,.2f}")
#             y_pos -= 20
        
#         c.save()
#         return pdf_filename

#     # Print Report Button
#     if st.button("🖨 Print Monthly Report"):
#         pdf_file = generate_monthly_pdf()
#         st.success("✅ Monthly report generated successfully!")
#         st.download_button("📥 Download Monthly Report", data=open(pdf_file, "rb"), file_name=pdf_file, mime="application/pdf")

# else:
#     st.info("📌 No data recorded for this month yet.")

# # ---- FOOTER ----
# st.markdown('<div class="footer">🔹 Developed by Lasani Embroidery | All Rights Reserved © 2025</div>', unsafe_allow_html=True)
import streamlit as st
import pandas as pd
from datetime import datetime
from reportlab.pdfgen import canvas

# ---- CONFIGURATION ----
st.set_page_config(page_title="Lasani Embroidery - Monthly Stitch Report", page_icon="🧵", layout="wide")

# ---- COMPANY HEADER ----
st.markdown("""
    <style>
        .header { font-size:32px; font-weight:bold; color:#4CAF50; text-align:center; }
        .sub-header { font-size:20px; font-weight:bold; color:#FF9800; text-align:center; }
        .info-box { background-color:#f4f4f4; padding:10px; border-radius:5px; text-align:center; }
        .footer { text-align:center; font-size:14px; color:#888; margin-top:20px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">🧵 Lasani Embroidery - Monthly Stitch Report & Bonus Calculator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">📌 Track Daily Stitch Production, Earnings & Bonus</div>', unsafe_allow_html=True)

st.divider()

# ---- CONSTANTS ----
COST_PER_100K_STITCHES = 250  # Rs. 250 per 100,000 stitches
BONUS_THRESHOLD = 400000  # Bonus given after 400,000 stitches per day
BONUS_AMOUNT = 100  # Rs. 100 bonus if stitches exceed 400,000 per day

# ---- SESSION STATE FOR MONTHLY DATA ----
if "monthly_data" not in st.session_state:
    st.session_state.monthly_data = []

# ---- USER INPUTS ----
st.subheader("📋 Employee & Machine Details")

employee_name = st.text_input("👤 Employee Name", placeholder="Enter worker's name")
machine_number = st.text_input("⚙️ Machine Number", placeholder="Enter machine number")
attendance = st.radio("📅 Attendance", ["Present", "Absent"], index=0, horizontal=True)
shift_time = st.selectbox("⏰ Shift Duration", ["Day Shift (8 AM - 8 PM)", "Night Shift (8 PM - 8 AM)"])
stitch_count = st.number_input("🧵 Enter total stitches for today:", min_value=0, value=100000, step=1000)

# ---- CALCULATION LOGIC ----
cost = (stitch_count / 100000) * COST_PER_100K_STITCHES
bonus = BONUS_AMOUNT if stitch_count >= BONUS_THRESHOLD else 0
total_earning = cost + bonus

# ---- SAVE DAILY RECORD ----
if st.button("💰 Save Today's Record"):
    if employee_name.strip() == "" or machine_number.strip() == "":
        st.warning("⚠️ Please enter both the employee's name and machine number.")
    else:
        today_date = datetime.now().strftime("%Y-%m-%d")
        st.session_state.monthly_data.append({
            "Date": today_date,
            "Employee": employee_name,
            "Machine": machine_number,
            "Shift": shift_time,
            "Attendance": attendance,
            "Stitches": stitch_count,
            "Base Cost": round(cost, 2),
            "Bonus": round(bonus, 2),
            "Total Earnings": round(total_earning, 2)
        })
        st.success(f"✅ Record saved for {today_date}")

# ---- SHOW MONTHLY REPORT ----
st.subheader("📊 Monthly Stitch Report")
if len(st.session_state.monthly_data) > 0:
    df = pd.DataFrame(st.session_state.monthly_data)
    st.dataframe(df)

    # Calculate Total Monthly Summary
    total_stitches = df["Stitches"].sum()
    total_base_cost = df["Base Cost"].sum()
    total_bonus = df["Bonus"].sum()
    total_earnings = df["Total Earnings"].sum()

    st.markdown(f"""
    ### 📅 Monthly Summary
    - 🧵 **Total Stitches:** {total_stitches:,}
    - 💵 **Total Base Cost:** Rs. {total_base_cost:,.2f}
    - 🎁 **Total Bonus Earned:** Rs. {total_bonus:,.2f}
    - 💰 **Total Earnings:** Rs. {total_earnings:,.2f}
    """)

    # ---- DELETE RECORD FEATURE ----
    st.subheader("🗑️ Delete a Record")
    record_to_delete = st.selectbox("📅 Select a date to delete:", df["Date"].unique())

    if st.button("❌ Delete Record"):
        st.session_state.monthly_data = [record for record in st.session_state.monthly_data if record["Date"] != record_to_delete]
        st.success(f"✅ Record for {record_to_delete} deleted successfully!")
        st.experimental_rerun()  # Refresh page after deletion

    # ---- PRINT MONTHLY REPORT FUNCTION ----
    def generate_monthly_pdf():
        pdf_filename = f"Lasani_Embroidery_Report_{datetime.now().strftime('%Y-%m')}.pdf"
        c = canvas.Canvas(pdf_filename)
        
        c.setFont("Helvetica-Bold", 16)
        c.drawString(150, 800, "Lasani Embroidery - Monthly Stitch Report")
        
        c.setFont("Helvetica", 12)
        c.drawString(50, 770, f"Report Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        c.drawString(50, 750, f"Employee: {employee_name}")
        c.drawString(50, 730, f"Machine Number: {machine_number}")
        
        c.drawString(50, 700, f"Total Stitches: {total_stitches:,}")
        c.drawString(50, 680, f"Total Base Cost: Rs. {total_base_cost:,.2f}")
        c.drawString(50, 660, f"Total Bonus: Rs. {total_bonus:,.2f}")
        c.drawString(50, 640, f"Total Earnings: Rs. {total_earnings:,.2f}")

        c.drawString(50, 610, "Daily Breakdown:")
        y_pos = 590
        for index, row in df.iterrows():
            c.drawString(50, y_pos, f"{row['Date']} - {row['Stitches']} stitches - Rs. {row['Total Earnings']:,.2f}")
            y_pos -= 20
        
        c.save()
        return pdf_filename

    # Print Report Button
    if st.button("🖨 Print Monthly Report"):
        pdf_file = generate_monthly_pdf()
        st.success("✅ Monthly report generated successfully!")
        st.download_button("📥 Download Monthly Report", data=open(pdf_file, "rb"), file_name=pdf_file, mime="application/pdf")

else:
    st.info("📌 No data recorded for this month yet.")

# ---- FOOTER ----
st.markdown('<div class="footer">🔹 Developed by Lasani Embroidery | All Rights Reserved © 2025</div>', unsafe_allow_html=True)

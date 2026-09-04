import streamlit as st

# STYLING
def apply_styles():

    st.markdown(
        """
        <style>
        
        /* Subtle text shadow */
        h1, h2, h3, h4, h5, h6 {
            text-shadow: 0 1px 3px rgba(0, 0, 0, 0.35);
        }
        
        .stApp {
            background: linear-gradient(180deg,
                #0A1428 0%,
                #0F2148 16.6%,
                #15326A 33.3%,
                #1E4A8C 50%,
                #15326A 66.6%,
                #0F2148 83.3%,
                #0A1428 100%
                );
        }

        /* ====================================================
           MAIN PAGE
        ==================================================== */

        .block-container {
            max-width: 1400px;
            padding-top: 3rem;
            padding-bottom: 2rem;
        }


        /* ====================================================
           HEADER
        ==================================================== */

        h1 {
            margin-bottom: 0.25rem;
        }


        /* ====================================================
           INPUT FORM
        ==================================================== */

        div[data-testid="stForm"] {
            background-color: #151A22;
            border: 1px solid #2A313C;
            border-radius: 12px;
            padding: 12px;
        }


        /* ====================================================
           FORM BUTTON
        ==================================================== */

        div[data-testid="stFormSubmitButton"] button {
            width: 100%;
            height: 38px;
            border-radius: 7px;
            font-size: 14px;
            font-weight: 600;
        }


        /* ====================================================
           DROPDOWN
        ==================================================== */

        div[role="listbox"] {
            max-height: 220px !important;
            overflow-y: auto !important;
        }


        /* ====================================================
           PREDICTION METRIC BOXES
        ==================================================== */

        div[data-testid="stMetric"] {
            background-color: #151A22;
            border: 1px solid #2A313C;
            border-radius: 12px;
            padding: 20px;
        }


        /* ====================================================
           SMALL SCREEN / TABLET
        ==================================================== */

        @media (max-width: 900px) {

            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
                padding-top: 3rem;
                padding-bottom: 3rem;
            }

            h1 {
                font-size: 1.8rem !important;
                text-align: center !important;
            }

            h2 {
                font-size: 1.4rem !important;
                text-align: center !important;
            }

            h3 {
                font-size: 1.15rem !important;
                text-align: center !important;
            }

            h4 {
                font-size: 1rem !important;
                text-align: center !important;
            }

            h5 {
                font-size: 0.85rem !important;
                text-align: center !important;
            }

            p,
            label {
                font-size: 0.85rem !important;
            }

            div[data-testid="stMetric"] {
                padding: 14px;
            }

            div[data-testid="stMetricLabel"] {
                font-size: 0.75rem !important;
            }

            div[data-testid="stMetricValue"] {
                font-size: 1.5rem !important;
            }

            div[data-testid="stForm"] {
                padding: 10px;
            }

            div[data-testid="stFormSubmitButton"] button {
                height: 40px;
                font-size: 13px;
            }
            
            div[data-testid="stVegaLiteChart"] {
                height: 150px !important;
            }

            div[data-testid="stVegaLiteChart"] iframe {
                height: 150px !important;
            }
        }


        /* ====================================================
           VERY SMALL SCREEN / MOBILE
        ==================================================== */

        @media (max-width: 600px) {

            .block-container {
                padding-left: 0.7rem;
                padding-right: 0.7rem;
                padding-top: 3rem;
                padding-bottom: 4rem;
            }

            h1 {
                font-size: 1.5rem !important;
                text-align: center !important;
            }

            h2 {
                font-size: 1.2rem !important;
                text-align: center !important;
            }

            h3 {
                font-size: 1rem !important;
                text-align: center !important;
            }

            h5 {
                font-size: 0.75rem !important;
                text-align: center !important;
            }

            p,
            label {
                font-size: 0.78rem !important;
            }

            div[data-testid="stMetric"] {
                padding: 12px;
                border-radius: 9px;
            }

            div[data-testid="stMetricLabel"] {
                font-size: 0.7rem !important;
            }

            div[data-testid="stMetricValue"] {
                font-size: 1.25rem !important;
            }

            div[data-testid="stForm"] {
                padding: 8px;
            }

            div[data-testid="stFormSubmitButton"] button {
                height: 38px;
                font-size: 12px;
                text-align: center !important;
            }
        }

        </style>
        """,
        unsafe_allow_html=True
    )

# HEADER
def show_header():

    st.markdown(
        "<h1 style='text-align: center;'>VEHICLE PRICE PREDICTOR</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h5 style='text-align: center;'>Random Forest vs Gradient Boosting</h5>",
        unsafe_allow_html=True
    )


# VEHICLE INPUTS
def show_vehicle_inputs():

    st.markdown(
        "<h3 style='text-align: center;'>ENTER VEHICLE DETAILS</h3>",
        unsafe_allow_html=True
    )

    with st.form("vehicle_prediction_form"):

        col1, col2 = st.columns(2)

        # LEFT COLUMN
        with col1:

            brand_name = st.selectbox(
                "Brand",
                [
                    "ashok leyland",
                    "aston martin",
                    "audi",
                    "bajaj",
                    "bentley",
                    "bmw",
                    "chevrolet",
                    "citroen",
                    "datsun",
                    "dc",
                    "ferrari",
                    "fiat",
                    "force",
                    "ford",
                    "hindustan motors",
                    "honda",
                    "hummer",
                    "hyundai",
                    "icml",
                    "isuzu",
                    "jaguar",
                    "jeep",
                    "kia",
                    "lamborghini",
                    "land rover",
                    "lexus",
                    "mahindra",
                    "mahindra renault",
                    "mahindra ssangyong",
                    "maruti",
                    "maserati",
                    "mercedes-benz",
                    "mg",
                    "mini",
                    "mitsubishi",
                    "nissan",
                    "opel",
                    "porsche",
                    "premier",
                    "renault",
                    "rolls-royce",
                    "skoda",
                    "tata",
                    "toyota",
                    "volkswagen",
                    "volvo"
                ],
                index=29
            )

            model_year = st.number_input(
                "Model Year",
                min_value=1980,
                max_value=2026,
                value=2020,
                step=1
            )

            transmission_type = st.selectbox(
                "Transmission",
                ["Manual", "Automatic"]
            )

            engine_cc = st.number_input(
                "Engine CC",
                min_value=500,
                max_value=10000,
                value=1197,
                step=1
            )

            max_power = st.number_input(
                "Max Power",
                min_value=1.0,
                value=88.0,
                step=1.0
            )

            max_torque = st.number_input(
                "Max Torque",
                min_value=1.0,
                value=113.0,
                step=1.0
            )


        # RIGHT COLUMN
        with col2:
            mileage = st.number_input(
                "Mileage",
                min_value=1.0,
                value=18.9,
                step=0.1
            )

            km_driven = st.number_input(
                "Kilometres Driven",
                min_value=0,
                value=40000,
                step=1000
            )

            kerb_weight = st.number_input(
                "Kerb Weight",
                min_value=100,
                value=1100,
                step=50
            )

            seller_type = st.selectbox(
                "Seller Type",
                ["Dealer", "Individual"]
            )

            car_segment = st.selectbox(
                "Car Segment",
                [
                    "Convertibles",
                    "Coupe",
                    "Hatchback",
                    "Hybrids",
                    "Luxury Vehicles",
                    "MUV",
                    "Minivans",
                    "Pickup Trucks",
                    "SUV",
                    "Sedan",
                    "Wagon"
                ],
                index=2
            )

        # PREDICT BUTTON
        submitted = st.form_submit_button(
            "Predict Price",
            use_container_width=True
        )

    # RETURN INPUTS
    if submitted:

        return {
            "brand_name": brand_name,
            "model_year": model_year,
            "transmission_type": transmission_type,
            "engine_cc": engine_cc,
            "max_power": max_power,
            "max_torque": max_torque,
            "mileage": mileage,
            "km_driven": km_driven,
            "kerb_weight": kerb_weight,
            "seller_type": seller_type,
            "car_segment": car_segment
        }

    return None
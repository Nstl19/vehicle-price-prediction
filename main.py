import streamlit as st
import pandas as pd
import altair as alt

from app.frontend.ui import (
    apply_styles,
    show_header,
    show_vehicle_inputs
)

from app.backend.preprocessing import prepare_input
from app.backend.prediction import predict_prices


# PAGE CONFIGURATION
st.set_page_config(
    page_title="Vehicle Price Predictor",
    page_icon="🚗",
    layout="wide"
)

# FRONTEND SETUP
apply_styles()
show_header()

# LAYER 1
input_col, result_col = st.columns(
    [1, 1.35],
    gap="large"
)

# VEHICLE INPUTS
with input_col:
    inputs = show_vehicle_inputs()

# PREDICTION RESULTS & COMPARISON
with result_col:
    if inputs is not None:
        
        user_features = prepare_input(
            model_year=inputs["model_year"],
            transmission_type=inputs["transmission_type"],
            engine_cc=inputs["engine_cc"],
            max_power=inputs["max_power"],
            max_torque=inputs["max_torque"],
            mileage=inputs["mileage"],
            brand_name=inputs["brand_name"],
            seller_type=inputs["seller_type"],
            car_segment=inputs["car_segment"],
            km_driven=inputs["km_driven"],
            kerb_weight=inputs["kerb_weight"]
        )

        rf_prediction, gb_prediction = predict_prices(
            user_features
        )

        st.markdown("<h3 style='text-align: center;'>PREDICTION RESULTS</h3>", unsafe_allow_html=True)

        prediction_col1, prediction_col2 = st.columns(2)

        with prediction_col1:

            st.markdown("<h4 style='text-align: center;'>🌳 Random Forest</h4>", unsafe_allow_html=True)

            st.metric(
                label="Estimated Vehicle Price",
                value=f"₹{rf_prediction:,.0f}"
            )


        with prediction_col2:

            st.markdown("<h4 style='text-align: center;'>📈 Gradient Boosting</h4>", unsafe_allow_html=True)

            st.metric(
                label="Estimated Vehicle Price",
                value=f"₹{gb_prediction:,.0f}"
            )
            
        st.markdown(
            """
            <div style="
                height: 1px;
                background: rgba(128, 128, 128, 0.30);
                margin: 18px 0 16px 0;
            "></div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<h3 style='text-align: center;'>PREDICTION COMPARISON</h3>", unsafe_allow_html=True)

        comparison_data = pd.DataFrame({
            "Algorithm": [
                "Random Forest",
                "Gradient Boosting"
            ],
            "Predicted Price": [
                rf_prediction,
                gb_prediction
            ]
        })

        chart = (
            alt.Chart(comparison_data)
            .mark_bar()
            .encode(
                x=alt.X(
                    "Algorithm:N",
                    sort=None,
                    title=None,
                    axis=alt.Axis(
                        labelAngle=0,
                        labelFontSize=12,
                        labelPadding=8
                    )
                ),
                y=alt.Y(
                    "Predicted Price:Q",
                    title="Price (₹)",
                    axis=alt.Axis(
                        format="~s",
                        labelFontSize=11
                    )
                ),
                tooltip=[
                    alt.Tooltip(
                        "Algorithm:N",
                        title="Model"
                    ),
                    alt.Tooltip(
                        "Predicted Price:Q",
                        title="Predicted Price",
                        format=",.0f"
                    )
                ]
            )
            .properties(
                height=300,
                padding={
                    "top": 5,
                    "bottom": 5,
                    "left": 5,
                    "right": 5
                }
            )
        )

        st.altair_chart(
            chart,
            use_container_width=True
        )

    else:

        st.markdown("<h3 style='text-align: center;'>PREDICTION RESULTS</h3>", unsafe_allow_html=True)
        st.info(
            "Enter the vehicle details and click "
            "**Predict Price** to see the results."
        )

# LAYER 2
if inputs is not None:
    st.divider()
    st.markdown("<h3 style='text-align: center;'>BETTER PERFORMING MODEL</h3>", unsafe_allow_html=True)

    st.success(
        "Gradient Boosting is the better-performing model "
        "based on test-set evaluation."
    )

    performance_col1, performance_col2, performance_col3 = (
        st.columns(3)
    )

    with performance_col1:

        st.metric(
            "R² Score",
            "0.6586"
        )

    with performance_col2:

        st.metric(
            "RMSE",
            "₹6,24,888"
        )

    with performance_col3:

        st.metric(
            "MAE",
            "₹2,72,115"
        )
        

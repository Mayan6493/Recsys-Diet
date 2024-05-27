import streamlit as st
from tkinter import Image

st.set_page_config(
    page_title="Personal Diet Plans",
    page_icon="🥗",
)

image_url = 'https://www.fitterfly.com/blog/wp-content/uploads/2022/05/blog-img-v1-2.jpg'

st.image(image_url, use_column_width=True)

st.markdown("\n\n-----------------------------------------------------------------------------\n\n")

st.write("# Your personal Diet Recommender!")

st.sidebar.success("Towards a Healthy Lifestyle")

st.markdown(
    """
    A diet recommendation web application using content-based approach with Scikit-Learn, FastAPI and Streamlit.
    """
)

st.write("## What is Our Diet Recommendation System?")

st.markdown(
    """
        Our diet recommendation system is a cutting-edge platform designed to provide personalized nutrition plans tailored to your unique needs and goals. Whether you're looking to lose weight, build muscle, manage a health condition, or simply eat healthier, our system offers expert guidance and support to help you achieve lasting results.
    """
)

st.write("### How It Works")

st.markdown(
    """
        1. **Sign Up and Create Your Profile**: Start by signing up and completing a comprehensive profile. You'll provide information about your health goals, dietary preferences, lifestyle, and any specific requirements or restrictions you may have.
        
        2. **Personalized Meal Plans**: Based on your profile, our advanced algorithms and expert nutritionists craft a customized meal plan that suits your needs. These plans are designed to be nutritionally balanced, easy to follow, and tailored to your taste preferences.

        3. **Receive and Follow Your Plan**: Access your personalized meal plan through our user-friendly platform. You'll receive detailed daily menus, shopping lists, and recipes that make it simple to stick to your plan and enjoy delicious, healthy meals.

        4. **Track Your Progress**: Monitor your progress with our built-in tracking tools. Log your meals, track your weight and other metrics, and receive regular feedback and adjustments to ensure you stay on track toward your goals.

        5. **Get Support and Motivation**: Join our community of like-minded individuals and get support from our team of nutrition experts. Participate in forums, attend webinars, and find the encouragement you need to succeed.
    """
)

st.write("### Benefits of Using Our System")

st.markdown(
    """
        - **Personalization**: Get meal plans that are tailored specifically to your needs and preferences, ensuring you enjoy what you eat while meeting your health goals.
        - **Expert Guidance**: Benefit from the knowledge and experience of professional nutritionists who design your plan and provide ongoing support.
        - **Convenience**: Enjoy the ease of having a structured plan with ready-made shopping lists and recipes, saving you time and effort.
        - **Accountability**: Stay motivated and accountable with progress tracking tools and regular feedback to keep you on the path to success.
        - **Community**: Connect with a supportive community for advice, motivation, and shared experiences, making your journey enjoyable and sustainable.

        Start your journey to better health today with our diet recommendation system and discover the power of personalized nutrition!
    """
)

st.markdown("\n\n-----------------------------------------------------------------------------\n\n")

st.write("## Featued Diet Plans")
st.write("")
st.write("")

def clickable_image(image_url, link_url, caption, border_style="2px solid white"):
    
    html_code = f'''
    <style>
    .zoom-container {{
        position: relative;
        width: 100%;
        overflow: hidden;
    }}
    .zoom-image {{
        transition: transform 0.5s ease;
        border: {border_style};
    }}
    .zoom-container:hover .zoom-image {{
        transform: scale(1.2);
    }}
    </style>
    <a href="{link_url}" target="_blank">
        <div class="zoom-container">
            <img src="{image_url}" alt="{caption}" class="zoom-image" style="width:100%; height:auto;">
        </div>
    </a>
    <div style="text-align:center">{caption}</div>
    '''
    return html_code

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(clickable_image("https://thumbor.forbes.com/thumbor/fit-in/x/https://www.forbes.com/health/wp-content/uploads/2021/05/Best_Diets-_Mediterrnean_Diet.jpeg", "https://www.healthline.com/nutrition/mediterranean-diet-meal-plan", "Mediterranean Diet"), unsafe_allow_html=True)

with col2:
    st.markdown(clickable_image("https://thumbor.forbes.com/thumbor/fit-in/x/https://www.forbes.com/health/wp-content/uploads/2021/05/DASH_DIET.jpeg", "https://www.healthline.com/nutrition/dash-diet", "DASH Diet"), unsafe_allow_html=True)

with col3:
    st.markdown(clickable_image("https://thumbor.forbes.com/thumbor/fit-in/x/https://www.forbes.com/health/wp-content/uploads/2023/04/flexitarian.jpeg.jpg", "https://www.healthline.com/nutrition/flexitarian-diet-guide", "Flexitarian Diet"), unsafe_allow_html=True)
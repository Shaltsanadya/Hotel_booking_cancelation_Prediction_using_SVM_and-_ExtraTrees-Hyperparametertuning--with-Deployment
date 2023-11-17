import pickle
import streamlit as st

hotel_model=pickle.load(open('hotel_predictions.sav', 'rb'))

st.title('Prediction of Hotel Booking Cancelations')

col1,col2,col3= st.columns(3)
with col1:
    no_of_adults = st.text_input ('Enter the number of adults')
with col2:
    no_of_children = st.text_input('Enter the number of children')
with col3:
    no_of_weekend_nights= st.text_input('Enter the number of weekend nights')
with col1:
    no_of_week_nights= st.text_input('Enter the number of week nights')
with col2:
    type_of_meal_plan= st.text_input('Enter the type of meal plan')
with col3:
    required_car_parking_space= st.text_input('Enter the required car parking space')
with col1:
    room_type_reserved= st.text_input('Enter the room type reserved')
with col2:
    lead_time= st.text_input('Enter the lead time') 
with col3:
    arrival_year= st.text_input('Enter the arrival year')
with col1:
    market_segment_type= st.text_input('Enter the market segment type')
with col2:  
    repeated_guest= st.text_input('Enter the repeated guest')
with col3:
    no_of_previous_cancellations= st.text_input('Enter the number of previous cancellations')
with col1:
    no_of_previous_bookings_not_canceled= st.text_input('Enter the number of previous bookings not canceled')
with col2:
    avg_price_per_room= st.text_input('Enter the average price per room')
with col3:
    no_of_special_requests= st.text_input('Enter the number of special requests')

#code for the prediction
cancel_pred= ''

#create button
if st.button('Result'):
    hotel_prediction= hotel_model.predict([['no_of_weekend_nights', 'no_of_week_nights', 'type_of_meal_plan', 'required_car_parking_space', 'room_type_reserved', 'lead_time', 'arrival_year', 'market_segment_type', 'repeated_guest', 'no_of_previous_cancellations', 'no_of_previous_bookings_not_canceled','avg_price_per_room', 'no_of_special_requests']])    
    
    if (hotel_prediction[0]==0):
        cancel_pred= 'Not Cancelled'
    else:
        cancel_pred= 'Cancelled'
    st.success(cancel_pred)

    







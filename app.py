
import streamlit as st
import pickle
import pandas as pd
import requests
# fetch poster function
def fetch_poster(movie_name):
    api_key = "8dd49f51"
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={movie_name}"
    response = requests.get(url)
    data = response.json()
    if data.get("Response") == "True":
        return data.get("Poster")
    return "https://via.placeholder.com/300x450?text=No+Poster"

# Recommend function code 
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_name = movies.iloc[i[0]].title
        recommended_movies.append(movie_name)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_name))
    return recommended_movies,recommended_movies_posters


# we are using pickle lib to pass the list of movies list to the selectbox
 
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
# import for similarity
similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
'How would you like to be contacted',(movies['title'].values))

# button 
if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.markdown(
                f"<div style='height:80px'>{names[i]}</div>",
                unsafe_allow_html=True
            )
            st.image(posters[i], width=180)
    
    
    

    


    
    
    

    


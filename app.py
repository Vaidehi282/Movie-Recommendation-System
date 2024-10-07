import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=a14f5cdb4e3c9ae5ff8477bba7bdaea7'
    response = requests.get(url)
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']

def recommend(movie):
    index = new_df[new_df['title'] == movie].index[0]
    dis = similarity[index]
    movies_list = sorted(list(enumerate(dis)), reverse = True, key = lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = new_df['id'][i[0]]
        recommended_movies.append(new_df['title'][i[0]])
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

new_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = new_df['title'].values


similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
selected_movie = st.selectbox('Which movie you like to search?', (movies_list))

if st.button("recommend"):
    names, posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])


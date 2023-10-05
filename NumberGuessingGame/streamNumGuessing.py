import streamlit as st
import random
import math

st.set_page_config(page_title="Guess The Number")


def answer(max: int) -> int:
    st.session_state.total = round(math.log(max + 1, 2))
    return random.randint(1, max)


def init(max: int = 10, pastinit=False):
    if not pastinit:
        st.session_state.input = 0
        st.session_state.wins = 0
        st.session_state.cheatcode = 0
    st.session_state.ans = answer(max)
    st.session_state.tries = 0
    st.session_state.over = False


def restart():
    init(st.session_state.max, pastinit=True)
    st.session_state.input += 1


def main():
    st.title('Welcome to the Number Guessing Game! ')
    head, _ = st.columns([1, 0.3])
    head.write('Im thinking of a number between...')
    st.write("---")
    if 'ans' not in st.session_state:
        init()
    st.slider('Select Maximum Range ', min_value=10, max_value=100, value=10, key='max', on_change=restart)
    floor, result = st.empty(), st.empty()
    guess = floor.number_input('Enter your Guess', min_value=0, max_value=st.session_state.max,
                               key=st.session_state.input)
    if guess:
        flag = 0
        st.session_state.tries += 1
        st.session_state.total -= 1
        if guess < st.session_state.ans and st.session_state.total > 0:
            result.warning(f'{guess} ? try a higher number. You have {st.session_state.total} Guesses remaining')
        elif guess > st.session_state.ans and st.session_state.total > 0:
            result.warning(f'{guess} ? try a lower number. You have {st.session_state.total} Guesses remaining!')
        elif guess == st.session_state.ans:
            result.success(f'{guess} is correct ! It took you {st.session_state.tries} attempt(s)')
            flag = 1
            st.session_state.wins += 1
            st.session_state.over = True
            floor.empty()
            floor.button('Go Again!', on_click=restart)
        if st.session_state.total <= 0 and flag == 0:
            st.error(f'The number was {st.session_state.ans}')
            st.session_state.over = True
            floor.empty()
            floor.button('Try Again!', on_click=restart)


main()
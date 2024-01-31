# Imports

import os
import requests
from dotenv import load_dotenv

load_dotenv()
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from bip44 import Wallet
import web3
from web3 import Web3
from web3.auto.gethdev import w3 as web3


# Importing the following functions from the `crypto_wallet.py` file:
# * `generate_account`
# * `get_balance`
# * `send_transaction`

from crypto_wallet import generate_account, get_balance, send_transaction

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))


################################################################################
# KryptoJobs2Go Candidate Information

# Database of KryptoJobs2Go candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500

candidate_database = {
    "Lane": [
        "Lane",
        "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0",
        "4.3",
        0.20,
        "Images/lane.jpeg",
    ],
    "Ash": [
        "Ash",
        "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396",
        "5.0",
        0.33,
        "Images/ash.jpeg",
    ],
    "Jo": [
        "Jo",
        "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45",
        "4.7",
        0.19,
        "Images/jo.jpeg",
    ],
    "Kendall": [
        "Kendall",
        "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45",
        "4.1",
        0.16,
        "Images/kendall.jpeg",
    ],
}


# A list of the KryptoJobs2Go candidates first names

people = ["Lane", "Ash", "Jo", "Kendall"]


def get_people():
    """Display the database of KryptoJobs2Go candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("KryptoJobs2Go Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

################################################################################
# Streamlit Code

# Streamlit application headings

st.markdown("# KryptoJobs2Go!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")


################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")


# Calling the `generate_account` function and save it as the variable `account`

account = generate_account()


# Writing the client's Ethereum account address to the sidebar

st.sidebar.write(account.address)


##########################################

# Creating a select box to choose a FinTech Hire candidate

person = st.sidebar.selectbox("Select a Person", people)


# Creating a input field to record the number of hours the candidate worked

hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")


# Identifing the FinTech Hire candidate

candidate = candidate_database[person][0]


# Writing the KryptoJobs2Go candidate's name to the sidebar

st.sidebar.write(candidate)


# Identifying the KryptoJobs2Go candidate's hourly rate

hourly_rate = candidate_database[person][3]


# Writing the FinTech Finder candidate's hourly rate to the sidebar

st.sidebar.write(hourly_rate)


# Identify the KryptoJobs2Go candidate's Ethereum Address

candidate_address = candidate_database[person][1]


# Write the inTech Finder candidate's Ethereum Address to the sidebar

st.sidebar.write(candidate_address)


# Write the KryptoJobs2Go candidate's name to the sidebar

st.sidebar.markdown("## Total Wage in Ether")


################################################################################

# Step 2: Signing and Executing a Payment Transaction

# Calculating total `wage` for the candidate by multiplying the candidate’s hourly
# rate from the candidate database (`candidate_database[person][3]`) by the
# value of the `hours` variable

wage = candidate_database[person][3] * hours


# Writing the `wage` calculation to the Streamlit sidebar

st.sidebar.write(wage)


# Creating a button to execute the payment transaction

if st.sidebar.button("Send Transaction"):
    # Calling the `send_transaction` function and passing the following values:
    # * The `account` variable
    # * The `candidate_address` variable
    # * The `wage` variable

    # Also 

    # Saving the returned transaction hash as a variable named `transaction_hash`

    transaction_hash = send_transaction(w3, account, candidate_address, wage)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()


# The function that starts the Streamlit application
# Writes KryptoJobs2Go candidates to the Streamlit page

get_people()


# Step 3: Inspecting the Transaction on Etherscan

# Sending a test transaction by using the application’s web interface, and then
# looking up the resulting transaction hash in Ganache.
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('Revolut Analytics')

uploaded_file = st.file_uploader("Choose a Revolut CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    all_transfers = df[(df['Type'] == 'TRANSFER') & (
        ~df['Description'].str.contains('To GBP'))]
    sent_transfers = all_transfers.groupby(
        ['Description']).sum()["Amount"].abs()

    all_topups = df[(df['Type'] == 'TOPUP')]
    recieved_topups = all_topups.groupby(['Description']).sum()["Amount"].abs()

    st.header("Transfer Summary")
    st.subheader("All Transfers")
    st.write(sent_transfers)

    st.subheader("Total Transfers per Person")
    fig, ax = plt.subplots()
    sent_transfers.plot(kind="bar", ax=ax)
    ax.set_xlabel("Person")
    ax.set_ylabel("Total Amount Transferred")
    ax.set_title("Total Amount Transferred per Person")
    st.pyplot(fig)

    st.subheader("All Topups")
    st.write(recieved_topups)

    st.subheader("Total Topups per Person")
    fig, ax = plt.subplots()
    recieved_topups.plot(kind="bar", ax=ax)
    ax.set_xlabel("Person")
    ax.set_ylabel("Total Amount Topup")
    ax.set_title("Total Amount Topup per Person")
    st.pyplot(fig)

    all_payments = df[(df['Type'] != 'TOPUP') & (
        ~df['Description'].str.contains('To GBP'))]
    sent_payments = all_payments.groupby(
        ['Description']).sum()["Amount"].abs()

    st.subheader("All Payments")
    st.write(sent_payments)

    st.subheader("Total Payments")
    fig, ax = plt.subplots()
    sent_payments.plot(kind="bar", ax=ax)
    ax.set_xlabel("Category")
    ax.set_ylabel("Total Payment Transferred")
    ax.set_title("Total Payment Transferred per Category")
    st.pyplot(fig)

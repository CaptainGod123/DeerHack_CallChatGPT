import React, { useState, useEffect } from 'react';
import axios from 'axios';

// import MessageCard from './MessageCard';

export default ({ convoList }) => {
  const url = 'http://127.0.0.1:5000/';

  return (
    <div
      style={{
        maxHeight: '88vh',
        overflow: 'auto',
        marginBottom: '50px',
        paddingTop: '10px',
      }}
    >
      {convoList.map((message, index) => {
        return (
          <div
            style={{
              display: 'flex',
              flexDirection: 'row',
              width: '100%',
            }}
          >
            <div
              style={{
                display: 'flex',
                flexDirection: 'column',
                width: '10%',
                justifyContent: 'flex-end',
                marginLeft: '-60px',
                paddingRight: '20px',
              }}
            >
              <div
                style={{
                  width: '100%',
                  display: 'flex',
                  flexDirection: 'row',
                  alignContent: 'flex-start',
                  justifyContent: 'flex-end',
                  marginBottom: '20px',
                }}
              >
                <img
                  src={
                    process.env.PUBLIC_URL +
                    (message.isGPT ? '/chat.png' : '/notgpt.jpeg')
                  }
                  style={{
                    maxWidth: '50%',
                    maxHeight: '100%',
                    borderRadius: '50%',
                  }}
                />
              </div>
            </div>
            <div style={{ flex: 1, maxWidth: '100%' }}>
              <MessageCard key={index} message={message} />
            </div>
          </div>
        );
      })}
    </div>
  );
};

const MessageCard = ({ message }) => {
  const cardStyle = {
    backgroundColor: message.isGPT ? '#aad2c7' : 'white',
    padding: '10px',
    border: '1px solid black',
    // maxWidth: '80%',
    margin: '0 auto',
    marginRight: '15px',
    marginBottom: '10px',
    borderRadius: '10px',
    fontFamily: 'sans-serif',
    fontSize: '20px',
  };
  return (
    <div style={cardStyle}>
      <p>
        {message.isGPT ? 'GPT' : 'You'} {'\u25CF '}
        {message.date}
      </p>
      <p>{message.message}</p>
    </div>
  );
};

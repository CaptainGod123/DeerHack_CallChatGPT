import React, { useState, useEffect } from 'react';
import axios from 'axios';

// import MessageCard from './MessageCard';

export default ({ phoneNumber }) => {
  const url = 'http://127.0.0.1:5000/';

  const [convoList, setConvoList] = useState([]);

  const sanitizedMessageData = (messageInfo) => {
    const date = messageInfo[0]?.trim();
    const isGPT = messageInfo[1]?.trim() === 'GPT';
    const message = messageInfo[2]?.trim();
    return { date, isGPT, message };
  };

  const updateConvoList = (messageInfo) => {
    const { date, isGPT, message } = sanitizedMessageData(messageInfo);
    if (date === '' && message === '') return;
    setConvoList((prev) => {
      return [
        ...prev,
        {
          date: date,
          isGPT: isGPT,
          message: message,
        },
      ];
    });
  };

  useEffect(() => {
    axios
      .get(url + '/users')
      .then((res) => {
        if (res.data.length > 0) {
          res.data.forEach((user) => {
            if (user?.phone_number === phoneNumber) {
              const individualMessages = user?.conversation.split(':::');
              individualMessages.forEach((individualMessage) => {
                const messageInfo = individualMessage.split(':-:');
                if (messageInfo.length === 3) {
                  updateConvoList(messageInfo);
                }
              });
            }
          });
        }
      })
      .catch((err) => console.error(err));
  }, []);

  useEffect(() => {
    console.log(convoList);
  }, [convoList]);

  return (
    <div>
      {convoList.map((message, index) => (
        <MessageCard key={index} message={message} />
      ))}
    </div>
  );
};

const MessageCard = ({ message }) => {
  const cardStyle = {
    backgroundColor: message.isGPT ? 'red' : 'white',
    padding: '10px',
    border: '1px solid black',
  };
  return (
    <div style={cardStyle}>
      <p>{message.date}</p>
      <p>{message.isGPT}</p>
      <p>{message.message}</p>
    </div>
  );
};

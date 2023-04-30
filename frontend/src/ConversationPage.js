import { useEffect, useState } from 'react';
import axios from 'axios';
import ChatBox from './ChatBox';
import NavBar from './NavBar';

// const phoneNumber = '+14169867125';
export const url = 'http://127.0.0.1:5000/';

function ConversationPage({ phoneNumber, setSelectedPhone }) {
  const [convoList, setConvoList] = useState([]);

  const handleReload = () => {
    setConvoList([]);
    fetchAllUserConvo();
  };
  useEffect(() => {
    fetchAllUserConvo();
  }, []);

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

  const fetchAllUserConvo = () => {
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
  };
  return (
    <div style={{ position: 'relative', minHeight: '100vh' }}>
      {/* <nav
        className='navBar'
        style={{
          position: 'sticky',
          top: '0',
          backgroundColor: '#1e3a58',
          color: '#fff',
          borderTopLeftRadius: '10px',
          borderTopRightRadius: '10px',
          zIndex: '1',
          height: '60px',
        }}
      >
        <div style={{ display: 'flex', justifyContent: 'center' }}>
          <h1
            style={{ margin: '0', padding: '1rem', fontFamily: 'sans-serif' }}
          >
            CallGPT
          </h1>
        </div>
      </nav> */}
      <NavBar
        phoneNumber={phoneNumber}
        handleReload={handleReload}
        handleLogout={() => setSelectedPhone(null)}
      />
      <div
        style={{
          position: 'absolute',
          top: '0',
          left: '0',
          right: '0',
          bottom: '15px',
          backgroundColor: '#8cadc6',
          marginTop: '60px',

          zIndex: 0,
        }}
      >
        <ChatBox convoList={convoList} />
      </div>
    </div>
  );
}

export default ConversationPage;

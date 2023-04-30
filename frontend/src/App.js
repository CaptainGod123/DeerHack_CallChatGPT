import { useEffect, useState } from 'react';
import axios from 'axios';
import ConversationPage, { url } from './ConversationPage';
import './App.css';

function App() {
  const [phone, setPhone] = useState('');
  const [password, setPassword] = useState('');
  const [allUsers, setAllUsers] = useState([]);

  const [selectedPhone, setSelectedPhone] = useState(null);
  const handleSubmit = (event) => {
    event.preventDefault();
    // Handle login logic here
    let phoneValue = phone;
    if (phoneValue.length > 0) {
      if (phoneValue[0] === '1') {
        phoneValue = '+' + phoneValue;
      }
      if (phoneValue[0] !== '+') {
        phoneValue = '+1' + phoneValue;
      }
    }
    allUsers.forEach((user) => {
      if (user[0] === phoneValue && user[1] === password) {
        setSelectedPhone(phoneValue);
      }
    });
  };

  useEffect(() => {
    // make api call to get all users
    axios
      .get(url + '/users')
      .then((res) => {
        if (res.data.length > 0) {
          res.data.forEach((user) => {
            const phone = user?.phone_number;
            const pass = user?.password;
            setAllUsers((prev) => [...prev, [phone, pass]]);
          });
        }
      })
      .catch((err) => console.error(err));
  }, []);

  if (selectedPhone !== null) {
    return (
      <ConversationPage
        phoneNumber={selectedPhone}
        setSelectedPhone={setSelectedPhone}
      />
    );
  }

  return (
    <div className='LoginPage'>
      <form className='LoginForm' onSubmit={handleSubmit}>
        <h2>Login</h2>
        <label>
          Phone number:
          <input
            type='text'
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
          />
        </label>
        <label>
          Password:
          <input
            type='password'
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
        <button type='submit'>Login</button>
      </form>
    </div>
  );
}
export default App;

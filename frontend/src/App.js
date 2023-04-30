import ChatBox from './ChatBox';

const phoneNumber = '+14169867125';

function App() {
  return (
    <div style={{ position: 'relative', minHeight: '100vh' }}>
      <nav
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
      </nav>
      <div
        style={{
          position: 'absolute',
          top: '0',
          left: '0',
          right: '0',
          bottom: '15px',
          borderRadius: '10px',
          backgroundColor: '#8cadc6',
          paddingTop: '60px',
        }}
      >
        <ChatBox phoneNumber={phoneNumber} />
      </div>
    </div>
  );
}

export default App;

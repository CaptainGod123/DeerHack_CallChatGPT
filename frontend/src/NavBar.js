import React from 'react';

function NavBar(props) {
  const buttonStyle = {
    padding: '10px 20px',
    backgroundColor: '#4CAF50',
    color: 'white',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    fontSize: '16px',
  };
  const logoutButtonstyle = {
    padding: '10px 20px',
    backgroundColor: '#d60e0e',
    color: 'white',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    fontSize: '16px',
  };
  return (
    <div
      style={{
        backgroundColor: '#1e3a58',
        height: '60px',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        paddingLeft: '10px',
        paddingRight: '10px',
        zIndex: 2,
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
        <button style={logoutButtonstyle} onClick={props.handleLogout}>
          Logout
        </button>
        <button style={buttonStyle} onClick={props.handleReload}>
          Reload data
        </button>
      </div>
      <div
        style={{
          textAlign: 'center',
          margin: '0',
          padding: '1rem',
          fontFamily: 'sans-serif',
          color: 'white',
        }}
      >
        <h1>CallGPT</h1>
      </div>
      <div
        style={{
          textAlign: 'center',
          margin: '0',
          padding: '1rem',
          fontFamily: 'sans-serif',
          color: 'white',
        }}
      >
        {props.phoneNumber}
      </div>
    </div>
  );
}

export default NavBar;

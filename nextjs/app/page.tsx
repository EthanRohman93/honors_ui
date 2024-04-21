import React from 'react';
import Layout from './layout';
import LoginForm from './components/login/LoginForm';

const LoginPage = () => {
  return (
    <Layout>
      <div className="safe-top rounded-border p-4">
        <h1 className="mb-4">Login or Create an Account</h1>
        <LoginForm />
      </div>
    </Layout>
  );
};

export default LoginPage;


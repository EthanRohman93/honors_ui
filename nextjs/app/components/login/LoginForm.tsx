'use client'
import React from 'react';
import InputField from './InputField';
import GenerateCredentials from './CredentialsButton';
import InfoBanner from './InfoBanner';

const LoginForm: React.FC = () => {
  return (
    <div className="login-form">
      <InfoBanner />
      <InputField id="username" label="Username" placeholder="Enter or generate a username" helpText="Username is temporary and anonymous." type="text" />
      <GenerateCredentials />
      <InputField id="password" label="Password" placeholder="Enter or generate a password" helpText="Password should be 8 characters with mixed case and numbers." type="password" />
      <button type="submit">Login / Register</button>
    </div>
  );
};

export default LoginForm;

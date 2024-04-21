import React from 'react';
import { useTooltip } from './TooltipContext';  // Adjust path as necessary

interface InputFieldProps {
  id: string;
  label: string;
  placeholder: string;
  helpText: string;
  type: string;
}

const InputField: React.FC<InputFieldProps> = ({ id, label, placeholder, helpText, type }) => {
  const { showTooltip, hideTooltip } = useTooltip();

  return (
    <div className="input-wrapper">
      <label htmlFor={id}>{label}</label>
      <input
        id={id}
        type={type}
        placeholder={placeholder}
        onFocus={() => showTooltip(helpText)}
        onBlur={hideTooltip}
      />
    </div>
  );
};

export default InputField;


import React, { createContext, useContext, useState } from 'react';

interface TooltipContextType {
  message: string;
  visible: boolean;
  showTooltip: (message: string) => void;
  hideTooltip: () => void;
}

const TooltipContext = createContext<TooltipContextType>(null!);

export const useTooltip = () => useContext(TooltipContext);

export const TooltipProvider: React.FC = ({ children }) => {
  const [message, setMessage] = useState('');
  const [visible, setVisible] = useState(false);

  const showTooltip = (msg: string) => {
    setMessage(msg);
    setVisible(true);
  };

  const hideTooltip = () => {
    setVisible(false);
  };

  return (
    <TooltipContext.Provider value={{ message, visible, showTooltip, hideTooltip }}>
      {children}
      {visible && <div className="tooltip">{message}</div>}
    </TooltipContext.Provider>
  );
};


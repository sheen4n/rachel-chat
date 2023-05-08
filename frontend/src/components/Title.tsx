import { Dispatch, useState, SetStateAction } from 'react';
import http from '../utils/http';
import ArrowRefresh from '../icons/ArrowRefresh';
import { Message } from './Controller';

type Props = {
  setMessages: Dispatch<SetStateAction<Message[]>>;
};

const Title = ({ setMessages }: Props) => {
  const [isResetting, setIsResetting] = useState(false);

  const resetConversation = async () => {
    setIsResetting(true);
    try {
      const res = await http.get('reset');
      if (res.status == 200) setMessages([]);
      else {
        console.log('Error in api for reset.');
      }
    } catch (error) {
      console.log((error as Error).message);
    }
    setIsResetting(false);
  };

  return (
    <div className='flex justify-between items-center w-full p-4 bg-gray-900 text-white font-bold shadow'>
      <div className='italic'>Victoria</div>
      <button
        className={'transition-all duration-300 text-blue-300 hover:text-pink-500 ' + (isResetting && 'animate-pulse')}
        onClick={resetConversation}
      >
        <ArrowRefresh />
      </button>
    </div>
  );
};

export default Title;

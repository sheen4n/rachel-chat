// import React from 'react'
import { useState } from 'react';
import Title from './Title';
import RecordMessage from './RecordMessage';
import http from '../utils/http';

export type Message = { sender: string; blobUrl: string };

const Controller = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [messages, setMessages] = useState<Message[]>([]);
  // const [blob, setBlob] = useState<string>("");
  const createBlobUrl = (data: BlobPart) => {
    const blob = new Blob([data], { type: 'audio/mpeg' });
    const url = window.URL.createObjectURL(blob);
    return url;
  };

  const handleStop = async (reqBlobUrl: string) => {
    setIsLoading(true);
    // Append recorded message to messages
    const myMessage = { sender: 'me', blobUrl: reqBlobUrl };
    const messagesArr = [...messages, myMessage];

    try {
      // Convert blob url to blob object
      const blobRes = await fetch(reqBlobUrl);
      const requestBlob = await blobRes.blob();
      const formData = new FormData();
      formData.append('file', requestBlob, 'myFile.wav');

      const response = await http.post<BlobPart>('post-audio', formData, {
        headers: { 'Content-Type': 'audio/mpeg' },
        responseType: 'arraybuffer',
      });

      const backendBlob = response.data;
      const audio = new Audio();
      audio.src = createBlobUrl(backendBlob);

      const responseMessage = { sender: 'victoria', blobUrl: audio.src };
      messagesArr.push(responseMessage);

      setMessages(messagesArr);

      audio.play();
    } catch (error) {
      console.log((error as Error).message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className='h-screen overflow-y-hidden'>
      <Title setMessages={setMessages} />
      <div className='flex flex-col justify-between h-full overflow-y-scroll pb-96'>
        {/* Conversation */}
        <div className='mt-5 px-5'>
          {messages.map(({ sender, blobUrl }, index) => (
            <div key={index + sender} className={'flex flex-col ' + (sender == 'me' && 'flex items-end')}>
              {/* Sender */}
              <div className='mt-4'>
                <p className={sender == 'me' ? 'text-right mr-2 italic text-green-500' : 'ml-2 italic text-blue-500'}>
                  {sender}
                </p>
                {/* Audio Message */}
                <audio src={blobUrl} className='appearance-none' controls />
              </div>
            </div>
          ))}

          {messages.length == 0 && !isLoading && (
            <div className='text-center font-light italic mt-10'>Start by sending a message...</div>
          )}

          {isLoading && (
            <div className='text-center font-light italic mt-10 animate-pulse'>Gimme a few seconds...</div>
          )}
        </div>

        {/* Recorder */}
        <div className='fixed bottom-0 w-full py-6 border-t text-center bg-gradient-to-r from-sky-500 to-green-500'>
          <div className='flex justify-center items-center w-full'>
            <RecordMessage handleStop={handleStop} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Controller;

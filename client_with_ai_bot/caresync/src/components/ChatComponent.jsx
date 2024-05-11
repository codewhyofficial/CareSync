import React, { useState, useRef, useEffect } from "react";
import logo from "../assets/logo.png";

function ChatComponent() {
  const [message, setMessage] = useState("");
  const [conversation, setConversation] = useState([]);
  const [isOpen, setIsOpen] = useState(true); // State to manage the visibility of the chat component
  const conversationContainerRef = useRef(null);

  // Function to scroll conversation container to the bottom
  const scrollToBottom = () => {
    if (conversationContainerRef.current) {
      conversationContainerRef.current.scrollTop =
        conversationContainerRef.current.scrollHeight;
    }
  };

  // Scroll to bottom when conversation updates
  useEffect(() => {
    scrollToBottom();
  }, [conversation]);

  const handleSendMessage = async () => {
    const newUserMessage = { message, fromUser: true };
    setConversation([...conversation, newUserMessage]); // Add user message to conversation
    setMessage(""); // Clear input after sending message

    try {
      const url = "http://127.0.0.1:5001/generate_response";
      const requestBody = {
        prompt: message,
      };

      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(requestBody),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const responseData = await response.json();
      const botResponse = { message: responseData.response, fromUser: false };
      setConversation((prevConversation) => [...prevConversation, botResponse]); // Add bot response to conversation without removing user's message
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const toggleChat = () => {
    setIsOpen(!isOpen); // Toggle the visibility of the chat component
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    handleSendMessage();
  };

  return (
    <>
      <header class="font-black">
        {/* http://127.0.0.1:5000/ */}
        <nav class="flex flex-row m-2">
          <div class="button">
            <a href="http://127.0.0.1:5000/"><img src={logo} class="h-16 px-8 " /></a>
          </div>
          <ul class="flex ml-auto space-x-4 justify-center items-center px-10">
            <li><a href="http://127.0.0.1:5000/" class="text-gray-800 hover:text-gray-600 transition duration-300">Home</a></li>
            <li><a href="/" class="text-gray-800 hover:text-gray-600 transition duration-300">Contact Us</a></li>
            <li><a href="/" class="text-gray-800 hover:text-gray-600 transition duration-300">About</a></li>
          </ul>
        </nav>
      </header>

      <div className="flex justify-center py-8"><img src={logo} alt="" width="200px" srcset="" /></div>
      <div className="text-center font-bold text-3xl mt-2 text-violet-500">CareSync AI</div>
      <div className="m-2">
        <div className="mx-auto ">
          <div
            ref={conversationContainerRef}
            className={`min-h-[300px] overflow-y-auto  rounded p-4 pb-20 ${
              isOpen ? "block" : "hidden"
            }`}
          >
            {conversation.map((item, index) => (
              <div key={index} className={`mb-2 text-left bg-stone-100 p-2 rounded-lg p`}>
                <span
                  className={`bg-${
                    item.fromUser ? "red-600" : "red-300"
                  } text-black p-2 rounded`}
                >
                  {item.fromUser ? "User : " : "CareSync AI : "}
                  {item.message}
                </span>
              </div>
            ))}
          </div>
          <form onSubmit={handleSubmit}>
            <div className={`fixed bottom-2 left-0 right-0 mx-auto w-max ${
              isOpen ? "block" : "hidden"
            }`}>
              <input
                type="text"
                placeholder="Type to chat with CareSync AI..."
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                className="px-4 py-2 rounded border border-gray-300 focus:outline-none md:w-96"
              />
              <button
                type="submit"
                className="bg-violet-500 text-white px-4 py-2 rounded hover:bg-violet-600 focus:outline-none m-2 duration-300 hover:scale-105"
              >
                Send
              </button>
              <button
                onClick={toggleChat}
                className="mt-2 bg-gray-300 text-gray-700 px-4 py-2 rounded hover:bg-gray-400 focus:outline-none duration-300 hover:scale-105"
              >
                Close
              </button>
            </div>
          </form>
        </div>
      </div>
    </>
  );
}

export default ChatComponent;

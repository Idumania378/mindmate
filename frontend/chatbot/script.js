document.addEventListener('DOMContentLoaded', function() {
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    
    // Function to add a message to the chat
    function addMessage(content, isUser) {
        const messageDiv = document.createElement('div');
        messageDiv.className = isUser ? 'message user-message' : 'message bot-message';
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.innerHTML = `<p>${content}</p>`;
        
        const timeDiv = document.createElement('div');
        timeDiv.className = 'message-time';
        timeDiv.textContent = getCurrentTime();
        
        messageDiv.appendChild(contentDiv);
        messageDiv.appendChild(timeDiv);
        chatMessages.appendChild(messageDiv);
        
        // Scroll to the bottom of the chat
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Function to show typing indicator
    function showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'typing-indicator';
        typingDiv.id = 'typing-indicator';
        typingDiv.innerHTML = '<span></span><span></span><span></span>';
        chatMessages.appendChild(typingDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Function to hide typing indicator
    function hideTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }
    
    // Function to get current time in HH:MM format
    function getCurrentTime() {
        const now = new Date();
        return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }
    
    // Function to handle sending a message
    async function sendMessage() {
        const message = userInput.value.trim();
        if (message === '') return;
        
        // Add user message to chat
        addMessage(message, true);
        userInput.value = '';
        
        // Show typing indicator
        showTypingIndicator();
        
        try {
            // Get bot response (using a free mental health API)
            const response = await getBotResponse(message);
            
            // Hide typing indicator and add bot response
            hideTypingIndicator();
            addMessage(response, false);
        } catch (error) {
            hideTypingIndicator();
            addMessage("I'm having trouble connecting right now. Please try again later.", false);
            console.error('Error:', error);
        }
    }
    
    // Function to get bot response from API
    async function getBotResponse(message) {
        // In a real implementation, you would connect to your backend which interfaces with Qwen AI
        // For this example, we'll use a free mental health advice API (mock implementation)
        
        // Mock API call with timeout to simulate network delay
        await new Promise(resolve => setTimeout(resolve, 1000 + Math.random() * 2000));
        
        // This is a mock response - in your actual implementation, you'll call your Flask backend
        // which then interfaces with Qwen AI
        return generateMentalHealthResponse(message.toLowerCase());
    }
    
    // Function to generate mock mental health responses
    function generateMentalHealthResponse(message) {
        if (message.includes('stress') || message.includes('stressed')) {
            return "Stress is a common experience. Have you tried deep breathing exercises? Inhale for 4 seconds, hold for 4, exhale for 6. Repeat this a few times. Would you like to talk more about what's causing your stress?";
        } else if (message.includes('anxious') || message.includes('anxiety')) {
            return "Anxiety can feel overwhelming. Remember, what you're feeling is valid. Grounding techniques can help - try naming 5 things you can see, 4 you can touch, 3 you can hear, 2 you can smell, and 1 you can taste. Would this help to try now?";
        } else if (message.includes('sad') || message.includes('depressed')) {
            return "I'm sorry you're feeling this way. It's important to acknowledge these feelings. Small steps like getting outside for a short walk or talking to someone you trust can make a difference. Would you like me to suggest some resources?";
        } else if (message.includes('happy') || message.includes('good')) {
            return "I'm glad to hear you're feeling positive! Celebrating good moments is important for mental wellbeing. Consider journaling about what's making you feel this way to reflect on later.";
        } else if (message.includes('help') || message.includes('support')) {
            return "If you need immediate support, please consider reaching out to a mental health professional. Would you like me to provide some resources or hotlines that might be helpful?";
        } else if (message.includes('sleep') || message.includes('tired')) {
            return "Sleep issues can significantly impact mental health. Maintaining a consistent sleep schedule and reducing screen time before bed can help. Are you having trouble falling asleep, staying asleep, or waking up tired?";
        } else {
            const genericResponses = [
                "I hear you. Would you like to share more about how you're feeling?",
                "Thank you for sharing. It's important to talk about these things. How has this been affecting you?",
                "I understand. Mental health is complex and everyone's experience is unique. What would be most helpful for you right now?",
                "That sounds challenging. Remember to be kind to yourself during difficult times. Would you like to explore coping strategies?",
                "I'm here to listen. Sometimes just expressing how we feel can be helpful. Would you like to continue sharing?"
            ];
            return genericResponses[Math.floor(Math.random() * genericResponses.length)];
        }
    }
    
    // Event listeners
    sendButton.addEventListener('click', sendMessage);
    
    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
});
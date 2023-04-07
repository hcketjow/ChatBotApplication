const popup = document.querySelector('.chat-popup');
const chatBtn = document.querySelector('.chat-btn');
const submitBtn = document.querySelector('.submit');
const chatArea = document.querySelector('.chat-area');
const inputElm = document.querySelector('input');
   

chatBtn.addEventListener('click', ()=>{
    popup.classList.toggle('show');
})

submitBtn.addEventListener('click', ()=>{
    let userInput = inputElm.value;
    let temp = `<div class="out-msg">
    <span class="my-msg">${userInput}</span>
    <img src="/media/firenet.png" class="avatar">
    </div>`;

    chatArea.insertAdjacentHTML("beforeend", temp);
    inputElm.value = '';

    // Send user message to server and get chatbot response
    $.get('/getResponse', {userMessage:userInput}).done(function(data){
        let returnedMessage = "<div class='income-msg'><span class='bot-msg' style='padding:5px;'>"+data+"</span><img src='media/bot.png' class='avatar'></div>";
        chatArea.insertAdjacentHTML("beforeend", returnedMessage);
    })

})

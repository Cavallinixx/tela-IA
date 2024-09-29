function showHistory(message,response){
        var historyBox = document.getElementById('chatTextarea')

        // My message
        var boxMyMessage = document.createElement('div')
        boxMyMessage.className = 'box-my-message'

        var myMessage = document.createElement('p')
        myMessage.className = 'my-message'
        myMessage.innerHTML = message

        boxMyMessage.appendChild(myMessage)

        historyBox.appendChild(boxMyMessage)

        // Response message
        var boxResponseMessage = document.createElement('div')
        boxResponseMessage.className = 'box-response-message'

        var chatResponse = document.createElement('p')
        chatResponse.className = 'response-message'
        chatResponse.innerHTML = response

        boxResponseMessage.appendChild(chatResponse)

        historyBox.appendChild(boxResponseMessage)

        // Levar scroll para o final
        historyBox.scrollTop = historyBox.scrollHeight
}
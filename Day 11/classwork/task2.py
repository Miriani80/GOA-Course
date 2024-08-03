#შექმენით საიტი სადაც გექნებათ 2 პარაგრაფი და 2 ღილაკი
#<!DOCTYPE html>
#<html lang="ka">
#<head>
    #<meta charset="UTF-8">
    #<meta name="viewport" content="width=device-width, initial-scale=1.0">
    #<title>ორი პარაგრაფი და ორი ღილაკი</title>
    #<style>
        #body {
            #font-family: Arial, sans-serif;
            #margin: 20px;
            #background-color: #f0f0f0;
        #}
        #.content 
            #background-color: white;
            #padding: 20px;
            #margin-top: 20px;
            #border-radius: 8px;
            #box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        
        #button 
            #background-color: #4CAF50;
            #color: white;
            #border: none;
            #padding: 10px 20px;
            #text-align: center;
            #text-decoration: none;
            #display: inline-block;
            #font-size: 16px;
            #margin: 10px 2px;
            #cursor: pointer;
            #border-radius: 4px;
        
    #</style>
#</head>
#<body>
    #<div class="content">
        #<p>ეს არის პირველი პარაგრაფი. აქ შეგიძლიათ დაწეროთ ნებისმიერი ტექსტი, რომელიც გინდათ რომ მომხმარებლებმა ნახონ.</p>
        #<button onclick="alert('პირველი ღილაკი დაჭერილია!')">პირველი ღილაკი</button>
        #<p>ეს არის მეორე პარაგრაფი. აქაც შეგიძლიათ განათავსოთ ნებისმიერი ინფორმაცია, რომელიც საჭიროა თქვენს ვებ-გვერდზე.</p>
        #<button onclick="alert('მეორე ღილაკი დაჭერილია!')">მეორე ღილაკი</button>
    #</div>
#</body>
#</html>

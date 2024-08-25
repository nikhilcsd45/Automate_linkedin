import{GoogleGenerativeAI} from '@google/GoogleGenerative-ai';
const genAi=new GoogleGenerativeAI("AIzaSyDfAbJmx0zH8IjEKYzvhIjDSXsbTL_NeF8")
const model=genAi.getGenerativeModel({
    model:"gemini-1.5-pro",
})
const text1= 'he is a good boy'
const text2= 'he is a bad boy'
const r=await model.generateContent("compare the texts and give the % in similirty text1,text2")
console.log(r.response.text());




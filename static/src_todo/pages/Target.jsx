import React from 'react'


// Part 2 
// 이벤트의 처리
export default function Target() {

  function showName() {
    console.log('Python')
  }

  // function showText(event) {
  //   console.log(event.target.value)
  // }

  function showText(text) {
    console.log(text)
  }

  return (
    <div>
      <h1>Hello</h1>
      
      {/* function 을 활용한 컴포넌트 함수처리 */}
      <button onClick={showName}>show name</button>

      {/* Arrow Function 으로 직접 함수처리 */}
      <button onClick={ () => {
        console.log(30);
      }}>show age</button>

      <br/>

      {/* <input type="text" onChange={showText}></input> */}
      <input type="text" onChange={ (event) => {
        const text = event.target.value;
        showText(text);
      }} />

    </div>
  )
}

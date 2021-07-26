import React, { useState } from 'react'
import UserName from './UserName';


// props 특정 객체 1개만 호출하는 경우 {} 객체표시를 활용
export default function PropState({age}) {
// export default function PropState(props) {
// console.log(props) => {age: 20}

  const [name, setName] = useState('Python');
  const msg = age > 29 ? "Adult" : "Young Age";

  return (
    <div>
      {/* props.age : init value */}
      <h2>{name} ({age}) : {msg}</h2>
      <UserName name={name} />

      {/* <button onClick={changeName}>Change</button> */}
      <button
        onClick={() => {
          setName((name === "Python") ? "Js" : "Python");
        }}
      >Change</button>
    </div>
  )
}
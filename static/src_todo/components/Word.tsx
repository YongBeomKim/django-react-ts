import React, { useState } from 'react'

interface IProps {
  word: any;
}

// function 에서 받을 때 
// {} 로 받아야만 Key 가 생기지 않는다
export default function Word({word: w}: IProps) {

  const [word, setWord] = useState(w);
  const [isShow, setIsShow] = useState(false)
  const [isDone, setIsDone] = useState(word.isDone)

  function toggleShow() {
    setIsShow(!isShow);
  }

  function toggleDone() {
    fetch(process.env.WORD_API + `${word.id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        ...word,
        isDone: !isDone,
      }),
    }).then(res => {
      if (res.ok) {
        setIsDone(!isDone);
      }
    })
  }

  return (
    <tr className={isDone ? "off" : ""}>
      <td>
        <input 
          type="checkbox" 
          checked={isDone}
          onChange={toggleDone}
        />
      </td>
      <td>{word.eng}</td>
      <td>{isShow &&  word.kor}</td>
      <td>
        <button onClick={toggleShow}>뜻 {isShow ? "숨기기" : "보기"}</button>
        <button className="btn_del">Delete</button>
      </td>
    </tr>
  )
}




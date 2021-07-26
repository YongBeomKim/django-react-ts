import React, { useRef, useState } from 'react'
import { useHistory } from "react-router-dom";
import useFetch from '../hooks/useFetch'



export default function CreateWord() {

  const days = useFetch(process.env.WORD_API);
  const history = useHistory()
  const [isLoading, setIsLoading] = useState(false)

  // current : 해당 객체의 속성에 접근
  // value : 속성의 value 를 호출
  // console.log(engRef.current.value)
  // console.log(korRef.current.value)
  // console.log(dayRef.current.value)
  const engRef = useRef(null);
  const korRef = useRef(null);
  const dayRef = useRef(null);

  // form 의 기본 자동변환 기능을 차단
  function onSubmit(event) {
    event.preventDefault();

    if (!isLoading) {
      setIsLoading(true)
      fetch(process.env.WORD_API, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          day : dayRef.current.value,
          eng : engRef.current.value,
          kor : korRef.current.value,
          isDone: false,
        }),
      }).then(res => {
        if (res.ok) {
          alert("생성이 완료 되었습니다.")
          history.push(`/${dayRef.current.value}`)
          setIsLoading(false)
        }
      })
    }
  }

  return (
    <form onSubmit={onSubmit}>
      <div className="input_area">
        <label>Eng</label>
        <input type="text" placeholder="computer" ref={engRef} />
      </div>
      <div className="input_area">
        <label>Kor</label>
        <input type="text" placeholder="컴퓨터" ref={korRef} />
      </div>
      <div className="input_area">
        <label>Day</label>
        <select ref={dayRef}>
          {days.map(day => (
            <option key={day.id} value={day.day}>
              {day.day}
            </option>
          ))}
        </select>
      </div>
      <button
        style={{
          opacity: isLoading ? 0.3 : 1
        }}
      >
        {isLoading ? "Saving.." : "저장하기"}
      </button>
    </form>
  )
}

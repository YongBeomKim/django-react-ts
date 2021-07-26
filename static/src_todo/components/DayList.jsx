import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import useFetch from '../hooks/useFetch';


export default function DayList() {

  const days = useFetch(process.env.WORD_API)

  if (days.length === 0){
    return <span>Loading...</span>
  }

  return (
    <>
    <ul className="list_day">
      {days.map(day => (
        <li key={day.id}>
          <Link to={`/day/${day.day}`}>Day {day.day}</Link>
        </li>
      ))}
    </ul>
    </>
  );
}


// useEffect() Hook 의 활용
// =============================================
// const [count, setCount] = useState(0);
// function countNumber() {
//   setCount(count + 1)
// }
// function updateData() {
//   setDays([
//     ...days,
//     {
//       id: Math.random(),
//       day: 1,
//     }
//   ]);
// }

// // rendering 완료 및 update 이후에 작동하는 Hook
// useEffect( () => {
//   console.log("Count Change");
// }, [count]); 
// // 의존성 배열을 특정하면 해당 객체변화시만 동작
// // 빈배열 두번째 입력시 최초만 실행

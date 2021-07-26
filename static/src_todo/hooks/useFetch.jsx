import React, { useState, useEffect } from 'react'


// Custom React Hook
export default function useFetch(url) {
  const [data, setData] = useState([])

  useEffect(() => {
    // 변수명 사용시 BackTick Key 활용
    // fetch(process.env.WORD_API + `${day}`)
    fetch(url)
      .then(response => {
        return response.json();
      })
      .then(data => {
        console.log(data)
        setData(data);
      })
    }, [url]);

  return data;
}

import React, { useState, useEffect} from 'react'
import { useParams } from 'react-router-dom'
import useFetch from '../hooks/useFetch'
import Word from './Word'

export default function Day() {

  // useParams : Get the "url params Props : String Data" 
  const {day} = useParams()
  const words = useFetch(process.env.WORD_API + `${day}`)

  return (
    <>
    <h2>Day  {day} 일차</h2>
      <table>
        <tbody>
          {words.map(word => (
            <Word key={word.id} word={word} />
          ))}
        </tbody>
      </table>
    </>

  )
}


// useParams : react router 의 Params 호출 Hook
// const day_data = useParams()
// console.log(day_data);

// const wordList = dummy.words.filter(word => (
//   word.day === Number(day)
// ))

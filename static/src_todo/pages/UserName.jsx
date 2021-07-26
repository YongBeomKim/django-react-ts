import React from 'react'

// PropState 에서 state 인 name 전달
// props 중 name 객체만 활용
export default function UserName({name}) {
  return (
    <div>
      Hello, {name}
    </div>
  )
}

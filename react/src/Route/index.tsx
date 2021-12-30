import React, {ReactElement} from 'react'
import { BrowserRouter, Route } from 'react-router-dom';
import { CSSTransition } from 'react-transition-group';
import Text from '../Components/App';


// Tips)) params 많은 route 먼저위치
const routes = [
  {path:'/', name:'Home', Component:Text},
]

interface Props {
  path: string
  name: string
  Component: (param: any) => ReactElement<any, any> | null
}

const index:React.FC = () => {
  return (
    <BrowserRouter>
      {routes.map(({path,name,Component}:Props) =>(
        <Route
          exact key={name} path={path}>{({match}) => {
            return(
              <CSSTransition
                in={match != null}
                timeout={1500}
                classNames="transition"
                unmountOnExit>
                  <Component />
              </CSSTransition>
            )
          }}</Route>
      ))}
      {/* <Switch>
        <Route path='/about/:year' component={Gallery} />
        <Route path='/main/:year' component={PortFolio} />
        <Route path='/' component={Home} />
      </Switch> */}
    </BrowserRouter>
  )
}
export default index;
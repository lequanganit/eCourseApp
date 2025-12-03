import { useState } from "react"
import Catogories from "../../components/Categories"
import Courses from "../../components/Courses"


const Home=()=>{
    const [cateId, setCateId] = useState()
    return(
        <>
            <Catogories setCateId={setCateId} />
            <Courses cateId={cateId}/>
        </>
        
    )
}
export default Home
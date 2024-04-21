import React from 'react';
import ProjectInfo from "../../components/project/ProjectInfo"

type ParamsType = {
    params: {
        wname: string;
    }
}

export function generateStaticParams() {
  return [{ wname: 'answer-bot' }, { pname: 'capstone' }]
}


const ProjectDetails = ({ params }: ParamsType) => {
    return ( 
        <div>
            <ProjectInfo pname={params.pname} />
        </div>
    )
}
export default ProjectDetails;

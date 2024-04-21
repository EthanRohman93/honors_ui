export interface Project {
  pname: string;
}

export type ProjectName = {
    pname: string;
}

export type ProjectDescription = {
    desc: string[];
}

export type ProjectProps = {
    params: {
        pname: string;
        title: string;
        description: string[];
    };
};

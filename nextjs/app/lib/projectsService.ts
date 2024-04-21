import { promises as fs } from 'fs';
import path from 'path';

export async function getProjectNames(): Promise<string[]> {
    const projectsDirPath = path.join(process.cwd(), 'public', 'project');
    try {
        const filenames = await fs.readdir(projectsDirPath);
        return filenames.map(filename => path.parse(filename).name);
    } catch (error) {
        console.error('Failed to read project directory:', error);
        return []; // Return an empty array or handle the error as needed
    }
}

export async function getProjectData(name: string): Promise<any> {
    const filePath = path.join(process.cwd(), 'public', 'project', `${name}.json`);
    try {
        const fileContents = await fs.readFile(filePath, 'utf8');
        return JSON.parse(fileContents);
    } catch (error) {
        console.error('Failed to read project file:', error);
        throw error; // Re-throw the error or handle it as needed
    }
}

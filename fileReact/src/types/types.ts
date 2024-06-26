export interface File {
  id: number;
  name: string;
  file: string;
  file_extension: string;
  parent?: number;  // Optional field
}

export interface Folder {
  id: number;
  name: string;
  files: File[];
  folders: Folder[];
  parent?: number;  // Optional field
}

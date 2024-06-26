import { useState, useEffect } from "react";
import "../CSS/App.css";
import APIService from "../functions/APIService";
import { File, Folder } from '../types/types.ts';

import { MdOutlineFolder } from "react-icons/md";
import { IoArrowBackSharp } from "react-icons/io5";
import { IoMdHome } from "react-icons/io";
//import { FaEllipsisV } from "react-icons/fa";


function App() {
  const [folders, setFolders] = useState<Folder[]>([]);
  const [files, setFiles] = useState<File[]>([]);
  const [directoryPath, setDirectoryPath] = useState<string>("~/");
  const [currentId, setCurrentId] = useState<number>(0);

  //const audioExtensions = ['.mp3', '.aac', '.ogg', '.wav', '.flac'];
  const imageExtensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'];

  async function getFolderById(id: number) {
    const res = await APIService.GetFolderById(id);
    return res?.data;
  }

  async function getFilesInFolder(id: number) {
    const res = await APIService.GetFilesFromFolder(id);
    return res?.data;
  }

  async function getParentId() {
    const res = await APIService.GetParentId(currentId);
    return res?.data;
  }

  useEffect(() => {
    if (folders.length <= 0) {
      getFolderById(currentId)
        .then(res => {
          console.log(res)
          setFolders(res)
        })
        .catch(err => {
          console.log(err)
        })
    }
    if (files.length <= 0) {
      getFilesInFolder(currentId)
        .then(res => {
          console.log(res)
          setFiles(res)
        })
        .catch(err => {
          console.log(err)
        })
    }
  }, [currentId])

  function resetDirectory(id: number) {
    setFolders([]);
    setFiles([]);
    setCurrentId(id);
  }

  function backButton() {
    if (currentId === 0) {
      return;
    } else {
      getParentId()
        .then(res => {
          if (res?.length > 0) {
            resetDirectory(res)
          } else {
            resetDirectory(0);
          }
        })
        .catch(err => {
          console.log(err)
        })
    }
  }

  return (
    <div className="App">
      <div className="navigation-div">
        {currentId === 0 ? (
          <IoMdHome className="home-icon" />
        ) : (
          <IoArrowBackSharp className="back-arrow" onClick={backButton} />
        )
        }
        <div className="directory-path">{directoryPath}</div>
      </div>
      {folders.length > 0 && folders.map((folder: Folder) => (
        <div
          className="folder-div"
          key={folder.id}
          onClick={() => resetDirectory(folder.id)}
        >
          <MdOutlineFolder className="folder-icon" />
          {folder.name}
        </div>
      ))}
      {files.length > 0 && files.map((file: File) => (
        <div className="file-div" key={file.id}>
          {file.name}{file.file_extension}
          {imageExtensions.includes(file.file_extension) &&
            <div className="img-wrapper">
              <img src={file.file} />
            </div>
          }
        </div>
      ))}
    </div>
  )
}

export default App

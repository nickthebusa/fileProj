import axios from "axios";

const siteName = "http://127.0.0.1:8000"

export default class APIService {

  static async GetFiles() {
    return axios
      .get(`${siteName}/api/files/`)
      .then(res => { return res })
      .catch(err => { return err })
  }

  static async GetFolders() {
    return axios
      .get(`${siteName}/api/folders/`)
      .then(res => { return res })
      .catch(err => { return err })
  }

  static async GetFolderById(id: number) {
    return axios
      .get(`${siteName}/api/get_folder_by_id/${id}`)
      .then(res => { return res })
      .catch(err => { return err })
  }

  static async GetFilesFromFolder(id: number) {
    return axios
      .get(`${siteName}/api/get_files_from_folder/${id}`)
      .then(res => { return res })
      .catch(err => { return err })
  }

  static async GetParentId(id: number) {
    return axios
      .get(`${siteName}/api/get_parent_id/${id}`)
      .then(res => { return res })
      .catch(err => { return err })
  }
}

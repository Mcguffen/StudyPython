var timeString = function(timestamp) {
    t = new Date(timestamp * 1000)
    t = t.toLocaleTimeString()
    return t
}


var commentsTemplate = function(comments) {
    var html = ''
    // log('comments = ', comments)
    for(var i = 0; i < comments.length; i++) {
        var c = comments[i]
        var id = c.id
        var content = c.content
        var weibo_id = c.weibo_id
        var t = `
            <div class="comment-cell" id='comment-${id}' data-comid=${id}>
                ${content}
                <button class='comment-delete'>删除</button>
            </div>
        `
        html += t
    }
    // log('html = ', html)
    return html
}


var insertComment = function(comment){
    // comments是对象
    // 返回一个div的comment盒子
    var c = comment
    var id = c.id
    var content = c.content
    var weibo_id = c.weibo_id
    // log('debug insertComment\n', id, content, weibo_id)
    var t = `
        <div class="comment-cell" id='comment-${id}' data-comid=${id} data-weibo_id = weibo_id>
            ${content}
        <button class='comment-delete'>删除</button>
        </div>
    `
    return t

}

var delete_element = function () {
    //传入元素的id
    //删除元素

}

var WeiboTemplate = function(Weibo) {
    var content = Weibo.content
    var titile = Weibo.title
    var id = Weibo.id
    var comments = commentsTemplate(Weibo.comments)
    // 为什么我获取不到data的值
    // <span class='weibo-content'>[WEIBO]${content}</span>
    // log('comments=', comments, typeof(comments))
    var t = `
        <div class='weibo-cell' id='weibo-${id}' data-id=${id}>
                <span class='weibo-title'>[title]${titile}</span>
            <button class="weibo-delete">删除微博</button>
            <button class="weibo-edit">edit</button>
            <div class="comment-list">
                ${comments}
            </div>
            <div class="comment-form">
                <input type="hidden" name="weibo_id" value="">
                <input class="comment-input">
                <br>
                <button class="comment-add">添加评论</button>
            </div>
        </div>
    `
    return t
    /*
    上面的写法在 python 中是这样的
    t = """
    var ces={
    content: "四大复活节",
    id: 28,
    weibo_id: 8
};
    <div class="Weibo-cell">
        <button class="Weibo-delete">删除</button>
        <span>{}</span>
    </div>
    """.format(Weibo)
    */
}

var insertWeibo = function(Weibo) {
    var WeiboCell = WeiboTemplate(Weibo)
    // 插入 Weibo-list
    var WeiboList = e('.weibo-list')
    WeiboList.insertAdjacentHTML('beforeend', WeiboCell)
}

var insertEditForm = function(cell) {
    var form = `
        <div class='weibo-edit-form'>
            <input class="weibo-edit-input">
            <button class='weibo-update'>更新</button>
        </div>
    `
    cell.insertAdjacentHTML('beforeend', form)
}

var loadWeibos = function() {
    // 调用 ajax api 来载入数据
    apiWeiboAll(function(r) {
        // console.log('load all', r)
        // 解析为 数组
        var Weibos = JSON.parse(r)
        // 循环添加到页面中
        for(var i = 0; i < Weibos.length; i++) {
            var Weibo = Weibos[i]
            insertWeibo(Weibo)
        }
    })
}

var bindEventWeiboAdd = function() {
    var b = e('#id-button-add-weibo')
    // 注意, 第二个参数可以直接给出定义函数
    b.addEventListener('click', function(){
        var input = e('#id-input-weibo')
        var title = input.value
        log('click add', title)
        var content = input.value
        var form = {
            'title': title,
            'content': content,
        }
        apiWeiboAdd(form, function(r) {
            // 收到返回的数据, 插入到页面中
            var Weibo = JSON.parse(r)
            insertWeibo(Weibo)
        })
    })
}

var bindEventWeiboDelete = function() {
    var WeiboList = e('.weibo-list')
    // 注意, 第二个参数可以直接给出定义函数
    WeiboList.addEventListener('click', function(event){
        var self = event.target
        // log('点击了delete', self, self.parentElement)
        if(self.classList.contains('weibo-delete')){
            // 删除这个 Weibo
            var WeiboCell = self.parentElement
            // log('删除的dataset id=', self.parentElement, '删除自己', self)
            var Weibo_id = WeiboCell.dataset.id
            apiWeiboDelete(Weibo_id, function(r){
                log('删除成功', Weibo_id)
                WeiboCell.remove()
            })
        }
    })
}

var bindEventWeiboEdit = function() {
    var WeiboList = e('.weibo-list')
    // 注意, 第二个参数可以直接给出定义函数
    WeiboList.addEventListener('click', function(event){
        var self = event.target
        // log('点击了bindEventWeiboEdit deit', self.parentElement)
        if(self.classList.contains('weibo-edit')){
            // 删除这个 Weibo
            var WeiboCell = self.parentElement
            insertEditForm(WeiboCell)
        }
    })
}

var bindEventWeiboUpdate = function() {
    var WeiboList = e('.weibo-list')
    // 注意, 第二个参数可以直接给出定义函数
    WeiboList.addEventListener('click', function(event){
        var self = event.target
        if(self.classList.contains('weibo-update')){
            //
            var editForm = self.parentElement
            // querySelector 是 DOM 元素的方法
            // document.querySelector 中的 document 是所有元素的祖先元素
            var input = editForm.querySelector('.weibo-edit-input')
            var title = input.value
            // 用 closest 方法可以找到最近的直系父节点
            var WeiboCell = self.closest('.weibo-cell')
            var Weibo_id = WeiboCell.dataset.id
            var form = {
                'id': Weibo_id,
                'title': title,
            }
            apiWeiboUpdate(form, function(r){
                log('更新成功', Weibo_id)
                var Weibo = JSON.parse(r)
                var selector = '#weibo-' + Weibo.id
                var WeiboCell = e(selector)
                log('WeiboCell=', WeiboCell)
                var titleSpan = WeiboCell.querySelector('.weibo-title')
                titleSpan.innerHTML = '[WEIBO]'  + Weibo.title
//                WeiboCell.remove()
            })
        }
    })
}

var bindEventCommentAdd = function () {
    var b = e('.weibo-list')
    // 注意, 第二个参数可以直接给出定义函数
    // log('debug bindEventCommitAdd- -', b)
    b.addEventListener('click', function(event){
        var self = event.target
        if(self.classList.contains('comment-add')){
            var commentForm = self.parentElement
            // querySelector 是 DOM 元素的方法
            // document.querySelector 中的 document 是所有元素的祖先元素
            var input = commentForm.querySelector('.comment-input')
            log('点击了 comment-input ', input)
            // var title = input.value
            // var input = e('.comment-input')
            var content = input.value
            // 用 closest 方法可以找到最近的直系父节点
            var WeiboCell = self.closest('.weibo-cell')
            var Weibo_id = WeiboCell.dataset.id
            log('点击了评论添加click add', commentForm.parentElement)
            var form = {
                'weibo_id': Weibo_id,
                'content': content,
            }
            apiCommentAdd(form, function(r) {
                // 收到返回的数据, 插入到页面中
                var Comment = JSON.parse(r)
                log('更新成功', Weibo_id, Comment)

                // 选择
                var selector = '#weibo-' + Comment.weibo_id
                // 获取要修改comment的weibo的id
                // 根据id找到weibocell
                // 在weibocell中 找到commlist
                // 替换commentlist的内容
                // var comment = commentsTemplate(Comment)
                var addedComment = insertComment(Comment)
                var weiboCell = e(selector)
                // log('commentList=', commentList, '|', Comment)
                var titleSpan = weiboCell.querySelector('.comment-list')
                // log('titleSpan=', titleSpan)
                // 将返回的数据添加到commentlist的最后面

                titleSpan.insertAdjacentHTML('beforeend', addedComment)
                // var selector = '#weibo-' + Weibo.id
                // var WeiboCell = e(selector)
                // log('WeiboCell=', WeiboCell)
                // var titleSpan = WeiboCell.querySelector('.weibo-title')
                // titleSpan.innerHTML = '[WEIBO]'  + Weibo.title
            })
        }
    })
}

var bindEventCommentDelete = function() {
    //
    var WeiboList = e('.weibo-list')
    // 注意, 第二个参数可以直接给出定义函数
    WeiboList.addEventListener('click', function(event){
        var self = event.target
        // log('点击了delete', self, self.parentElement)
        if(self.classList.contains('comment-delete')){
            // 删除这个 Weibo
            var WeiboCell = self.parentElement
            log('删除的dataset id=', self.parentElement, '删除自己', self)
            // var Weibo_id = WeiboCell.dataset.id
            // apiWeiboDelete(Weibo_id, function(r){
            //     log('删除成功', Weibo_id)
            //     WeiboCell.remove()
            })
        }
    })
}

var bindEvents = function() {
    bindEventWeiboAdd()
    bindEventWeiboDelete()
    bindEventWeiboEdit()
    bindEventWeiboUpdate()
    bindEventCommentAdd()
    bindEventCommentDelete()
}
var ces={
    content: "四大复活节",
    id: 28,
    weibo_id: 8
};
var __main = function() {
    bindEvents()
    loadWeibos()
}

__main()

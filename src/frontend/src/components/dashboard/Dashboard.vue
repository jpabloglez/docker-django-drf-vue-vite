<template>
    <div>
        <div class="row row-controls">
            <div class="col-xs-12 text-right">
                <span id="show-modal"
                      @click="newAnalysis('vol')"
                      class="btn btn-danger"
                      :class="{ 'disabled': user.analyses_left === 0 || user.permissions.indexOf('analysis-new') === -1}"
                      style="position: relative; top: -10px">
                    <i class="fa fa-plus" aria-hidden="true"></i> {{$t('analysis.atrophy')}}
                </span>
                <span id="show-modal_wmles"
                      @click="newAnalysis('wmles')"
                      class="btn btn-danger"
                      :class="{ 'disabled': user.analyses_left === 0 || user.permissions.indexOf('analysis-new') === -1}"
                      style="position: relative; top: -10px">
                    <i class="fa fa-plus" aria-hidden="true"></i> {{ $t('analysis.lesions') }}
                </span>

                <span class="text-right" style="position: relative; top: -10px">
                    <dropdown>
                        <button class="btn btn-danger dropdown-toggle" type="button" id="dropdown-actions-options" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true"
                                :class="{ 'disabled': user.analyses_left === 0 || user.permissions.indexOf('analysis-new') === -1}">
                            <i class="fa fa-plus" aria-hidden="true"></i>
                            <span>{{ $t('analysis.longitudinal') }}</span>
                            <span class="caret"></span>
                        </button>
                        <template slot="dropdown">

                            <li style="cursor: pointer">
                                <a id="show-modal_longitudinal_wmles"
                                   @click="searchAnalysis('wmles')"
                                   :class="{ 'disabled': user.analyses_left === 0 || user.permissions.indexOf('analysis-new') === -1}">
                                    <i class="fa fa-plus" aria-hidden="true"></i>
                                    {{ $t('analysis.lesions') }}
                                </a>
                            </li>
                        </template>
                    </dropdown>
                </span>
            </div>
        </div>
        <div class="panel panel-primary" style="border: none !important">
            <div class="panel-heading"><h2>{{ $t('analysis.analyses') }}</h2></div>
            <div class="panel-body">
                <div class="row">
                    <div class="col-xs-12 col-sm-4 col-md-4 col-lg-3">
                        <a @click="show_filters = show_filters ? false : true;getUsers()" class="btn btn-default"><i class="fa fa-filter" aria-hidden="true"></i> &nbsp;{{ $t('analysis.filters') }} <span class="caret"></span></a>
                    </div>

                  <div class="col-xs-12 col-md-4 col-sm-4 col-lg-6 text-center">
                    <div class="fixed-btn btn-group btn-group-horizontal" role="group">
                      <!--
                      <span style="cursor:pointer" class="nav-item" >
                        <a @click="showType('vol')" class="btn btn-primary" v-bind:class="classObject('vol')" >{{$t('analysis.atrophy')}}</a>
                      </span>
                      <span style="cursor:pointer" class="nav-item" >
                        <a @click="showType('wmles')" class="btn btn-primary" v-bind:class="classObject('wmles')">{{$t('analysis.lesions')}}</a>
                      </span>
                      <span style="cursor:pointer" class="nav-item" >
                        <a @click="showType('longit_wmles')" class="btn btn-primary" v-bind:class="classObject('longit_wmles')">{{$t('analysis.longitudinal')}}</a>
                      </span>-->

                      <label class="btn btn-primary" style="margin-right: 25px; border-radius: 4px;">
                      <input type="checkbox" id="vol" value="vol" v-model="checkedTypes" >
                      {{$t('analysis.atrophy')}}</label>

                      <label class="btn btn-primary" style="margin-right: 25px; border-radius: 4px;">
                      <input type="checkbox" id="wmles" value="wmles" v-model="checkedTypes" >
                      {{$t('analysis.lesions')}}</label>

                      <label class="btn btn-primary" style="border-radius: 4px;">
                      <input type="checkbox" id="longit_wmles" value="longit_wmles" v-model="checkedTypes" >
                      {{$t('analysis.longitudinal')}}</label>
                      <br>

                    </div>
                  </div>


                    <div class="col-xs-12 col-sm-4 col-md-4 col-lg-3">
                        <div class="form-group">
                            <input type="text" v-model="search" class="pull-right form-control" v-bind:placeholder="$t('default.search')">
                        </div>
                    </div>
                </div>
                <div v-show="show_filters" class="panel panel-default filters-box">
                    <div class="panel-body">
                        <div class="row">
                            <p style="margin-left: 12px"><strong>{{ $t('analysis.date') }}</strong></p>
                            <div class="col-xs-2 col-sm-2 col-lg-2 col-md-2">
                                <dropdown class="form-group">
                                    <div class="input-group">
                                        <input style="color: white"  class="btn btn-default btn-sm dropdown-toggle" data-toggle="dropdown" type="text" v-model="start_date">
                                        <div class="input-group-btn">
                                            <button type="button" id="dropdownMenu1" class="btn btn-default btn-sm dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-calendar" aria-hidden="true"></i></button>
                                        </div>
                                    </div>
                                    <template slot="dropdown">
                                        <li>
                                            <date-picker  v-model="start_date" :locale=locale  :today-btn="false" :clear-btn="false" :width=0.1 />
                                        </li>
                                    </template>
                                </dropdown>
                            </div>
                            <div class="col-xs-1 col-sm-1 col-lg-1 col-md-1"></div>
                            <div class="col-xs-2 col-sm-2 col-lg-2 col-md-2">
                                <dropdown class="form-group">
                                    <div class="input-group">
                                        <input style="color: white" class="btn btn-default btn-sm dropdown-toggle" data-toggle="dropdown" type="text" v-model="end_date">
                                        <div class="input-group-btn">
                                            <button   type="button" id="dropdownMenu2" class="btn btn-default btn-sm dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-calendar" aria-hidden="true"></i></button>
                                        </div>
                                    </div>
                                    <template slot="dropdown">
                                        <li>
                                            <date-picker v-model="end_date" :locale=locale  :today-btn="false" :clear-btn="false" :width=0.1 />
                                        </li>
                                    </template>
                                </dropdown>
                            </div>
                            <div class="col-xs-1 col-sm-1 col-lg-1 col-md-1"></div>
                            <div class="col-xs-2 col-sm-2 col-lg-2 col-md-2">
                                <button @click="start_date='';end_date='';fetchAnalyses()" style="margin-left: 10px" type="button"  class="btn btn-primary btn-sm">Reset</button>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-xs-12">
                                <div class="column pull-left archived">
                                    <p><strong>{{ $t('analysis.archived') }}</strong></p>
                                    <div class="btn-group" role="group">
                                        <div v-if="show_filters">
                                            <filter-archived-item :variable="filter" value="-1" v-bind:label="$t('default.any')"></filter-archived-item>
                                            <filter-archived-item :variable="filter" value="1" v-bind:label="$t('default.yes')"></filter-archived-item>
                                            <filter-archived-item :variable="filter" value="0" v-bind:label="$t('default.no')"></filter-archived-item>
                                        </div>
                                    </div>
                                </div>
                                <div class="clearfix"></div>
                                <ul class="column user-list pull-left" v-show="showUsersFilter">
                                    <p><strong>{{ $t('user.users') }} ( <a @click="setUsersSelected(true)">{{ $t('analysis.all') }}</a> | <a @click="setUsersSelected(false)">{{ $t('analysis.myself') }}</a> )</strong></p>
                                    <li v-for="(item,index) in users">
                                        <filter-user-item v-if="show_filters" :user="item"></filter-user-item>
                                    </li>
                                </ul>
                                <div class="clearfix"></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div style="height: 20px; width: 100%"></div>
                <ul v-show="stop" class="nav nav-tabs nav-justified"></ul>
                <div v-show="show" style="padding-top: 30px">
                    <div  class="text-center">
                        <scaleLoader
                                :loading=loading
                                :color=color
                        ></scaleLoader>
                    </div>
                </div>
                <my-analyses :analyses="analyses" :users="share" :type="type" :stop="stop" :show="show"></my-analyses>
                <div v-show="analyses.length > 0" class="pagination text-center" style="width: 100%">
                    <button class="btn btn-default" @click="fetchAnalyses(pagination.prev_page_url)"
                            :disabled="!pagination.prev_page_url">{{ $t('default.previous') }}</button>
                    <span>{{ $t('pagination.page_range', { start: pagination.current_page, total: pagination.last_page}) }}</span>
                    <button class="btn btn-default" @click="fetchAnalyses(pagination.next_page_url)"
                            :disabled="!pagination.next_page_url">{{ $t('default.next') }}
                    </button>
                </div>
            </div>
        </div>

        <modal-error401 v-show="showError401"> </modal-error401>

        <modal-share></modal-share>
        <modal-delete></modal-delete>

        <modal-new-analysis
                formType="vol" :a_type="type"
        ></modal-new-analysis>
        <modal-search-wmles :a_type="'wmles'" :analyses="analyses" ></modal-search-wmles>
        <div v-show="type === 'longit_wmles'" class="hidden-xs hidden-sm" style="position: fixed; left: 0px;bottom: 0px;background: transparent url('/images/logo/qubio-demo-logo.png') no-repeat; width: 274px; height: 107px; z-index: -2 !important;"></div>
    </div>
</template>